using System.Collections;
using System.Globalization;
using System.Reflection;
using System.Runtime.Loader;
using System.Security.Cryptography;
using System.Text.Json;
using Mir3DataAudit;

return Run(args);

static int Run(string[] args)
{
    try
    {
        var options = ParseArguments(args);
        Export(options.DatabasePath, options.OutputPath);
        return 0;
    }
    catch (Exception exception)
    {
        var cause = exception is TargetInvocationException { InnerException: not null }
            ? exception.InnerException
            : exception;
        Console.Error.WriteLine($"export failed: {cause.Message}");
        ReportCleanupFailure(exception, cause);
        return 1;
    }
}

static ExportOptions ParseArguments(string[] args)
{
    if (args.Length != 5 || args[0] != "export")
        throw new ArgumentException("usage: export --database <absolute System.db> --output <json>");

    string? database = null;
    string? output = null;
    for (var index = 1; index < args.Length; index += 2)
    {
        switch (args[index])
        {
            case "--database":
                database = args[index + 1];
                break;
            case "--output":
                output = args[index + 1];
                break;
            default:
                throw new ArgumentException("usage: export --database <absolute System.db> --output <json>");
        }
    }

    if (database is null || output is null)
        throw new ArgumentException("both --database and --output are required");

    if (!Path.IsPathFullyQualified(database))
        throw new ArgumentException("--database must be an absolute path");

    var databasePath = new FileInfo(Path.GetFullPath(database));
    if (!string.Equals(databasePath.Name, "System.db", StringComparison.Ordinal))
        throw new ArgumentException("--database filename must be exactly System.db");
    RejectLinkedDatabasePath(databasePath);
    if (!databasePath.Exists)
        throw new FileNotFoundException("database does not exist", databasePath.FullName);

    var outputPath = new FileInfo(Path.GetFullPath(output));
    if (outputPath.Exists || Directory.Exists(outputPath.FullName) || outputPath.LinkTarget is not null)
        throw new ArgumentException("--output must name a file that does not already exist");

    return new ExportOptions(databasePath, outputPath);
}

static void RejectLinkedDatabasePath(FileInfo databasePath)
{
    if (IsLinkOrReparsePoint(databasePath))
        throw new ArgumentException("--database must not be a symbolic link or reparse point");
    if (!databasePath.Exists)
        return;

    for (var directory = databasePath.Directory; directory is not null; directory = directory.Parent)
    {
        if (IsLinkOrReparsePoint(directory))
            throw new ArgumentException("--database must not have a symbolic-link or reparse-point ancestor");
    }
}

static bool IsLinkOrReparsePoint(FileSystemInfo path)
{
    path.Refresh();
    return path.LinkTarget is not null
        || path.Exists && (path.Attributes & FileAttributes.ReparsePoint) != 0;
}

static void Export(FileInfo databasePath, FileInfo outputPath)
{
    var repositoryRoot = FindRepositoryRoot();
    RegisterRepositoryAssemblyResolver(repositoryRoot);

    var databaseRoot = Path.Combine(Path.GetTempPath(), $"mir3-data-audit-{Guid.NewGuid():N}");
    var backupRoot = Path.Combine(Path.GetTempPath(), $"mir3-data-audit-backup-{Guid.NewGuid():N}");
    object? session = null;
    Exception? exportFailure = null;
    try
    {
        Directory.CreateDirectory(databaseRoot);
        var copiedDatabasePath = Path.Combine(databaseRoot, "System.db");
        var sourceHashBeforeCopy = ComputeSha256(databasePath.FullName);
        File.Copy(databasePath.FullName, copiedDatabasePath);
        var copiedDatabaseHash = ComputeSha256(copiedDatabasePath);
        var sourceHashAfterCopy = ComputeSha256(databasePath.FullName);
        DatabaseHashBinding.RequireMatch(sourceHashBeforeCopy, sourceHashAfterCopy, copiedDatabaseHash);

        var libraryAssembly = AssemblyLoadContext.Default.LoadFromAssemblyPath(
            Path.Combine(repositoryRoot, "Library.dll"));
        var sessionType = RequireType(libraryAssembly, "MirDB.Session");
        var sessionModeType = RequireType(libraryAssembly, "MirDB.SessionMode");
        var serverMode = Enum.Parse(sessionModeType, "Server", ignoreCase: false);
        var constructor = sessionType.GetConstructor(new[]
        {
            sessionModeType, typeof(Assembly[]), typeof(bool), typeof(string), typeof(string), typeof(string),
        }) ?? throw new InvalidOperationException("MirDB.Session constructor was not found");

        session = constructor.Invoke(new object[]
        {
            serverMode,
            new[] { libraryAssembly },
            false,
            string.Empty,
            EnsureTrailingSeparator(databaseRoot),
            EnsureTrailingSeparator(backupRoot),
        });
        var init = sessionType.GetMethod("Init", Type.EmptyTypes)
            ?? throw new InvalidOperationException("MirDB.Session.Init() was not found");
        init.Invoke(session, null);

        var itemType = RequireType(libraryAssembly, "Library.SystemModels.ItemInfo");
        var monsterType = RequireType(libraryAssembly, "Library.SystemModels.MonsterInfo");
        var setType = RequireType(libraryAssembly, "Library.SystemModels.SetInfo");

        var items = ReadCollection(sessionType, session, itemType)
            .OrderBy(item => ReadInt(item, "Index"))
            .Select(item => new ItemSnapshot(
                ReadInt(item, "Index"),
                ReadString(item, "ItemName"),
                ReadString(item, "ItemType"),
                ReadString(item, "RequiredClass"),
                ReadInt(item, "RequiredAmount"),
                ReadInt(item, "Image")))
            .ToList();
        var monsters = ReadCollection(sessionType, session, monsterType)
            .OrderBy(monster => ReadInt(monster, "Index"))
            .Select(monster => new MonsterSnapshot(
                ReadInt(monster, "Index"),
                ReadString(monster, "MonsterName"),
                ReadInt(monster, "Level"),
                ReadInt(monster, "AI"),
                ReadInt(monster, "Image"),
                ReadBool(monster, "IsBoss")))
            .ToList();
        var sets = ReadCollection(sessionType, session, setType)
            .OrderBy(set => ReadInt(set, "Index"))
            .Select(set => new SetSnapshot(
                ReadInt(set, "Index"),
                ReadString(set, "SetName"),
                ReadEnumerable(set, "SetGroups")
                    .OrderBy(group => ReadInt(group, "Index"))
                    .Select(group => new SetGroupSnapshot(
                        ReadString(group, "GroupName"),
                        ReadInt(group, "RequiredNumItems"),
                        ReadEnumerable(group, "SetGroupItems")
                            .OrderBy(setGroupItem => ReadInt(setGroupItem, "Index"))
                            .Select(setGroupItem => ReadString(
                                ReadRequiredProperty(setGroupItem, "SetGroupItemInfo"),
                                "ItemName"))
                            .ToList()))
                    .ToList()))
            .ToList();

        var document = new ExportDocument(
            new DatabaseSnapshot("Database/System.db", copiedDatabaseHash, DateTimeOffset.UtcNow),
            items,
            monsters,
            sets);
        if (outputPath.DirectoryName is { Length: > 0 })
            Directory.CreateDirectory(outputPath.DirectoryName);
        using var outputStream = new FileStream(outputPath.FullName, FileMode.CreateNew, FileAccess.Write, FileShare.None);
        JsonSerializer.Serialize(outputStream, document, new JsonSerializerOptions
        {
            WriteIndented = true,
            PropertyNamingPolicy = JsonNamingPolicy.CamelCase,
        });
    }
    catch (Exception exception)
    {
        exportFailure = exception;
        throw;
    }
    finally
    {
        ExportCleanup.Run(exportFailure,
            () => (session as IDisposable)?.Dispose(),
            () => DeleteTemporaryDirectory(databaseRoot),
            () => DeleteTemporaryDirectory(backupRoot));
    }
}

static void ReportCleanupFailure(Exception exception, Exception cause)
{
    var cleanupFailure = exception.Data[ExportCleanup.FailureDataKey]
        ?? cause.Data[ExportCleanup.FailureDataKey];
    if (cleanupFailure is Exception cleanupException)
        Console.Error.WriteLine($"export cleanup failed: {cleanupException.Message}");
}

static string FindRepositoryRoot()
{
    var directory = new DirectoryInfo(AppContext.BaseDirectory);
    while (directory is not null)
    {
        if (File.Exists(Path.Combine(directory.FullName, "Library.dll")))
            return directory.FullName;
        directory = directory.Parent;
    }

    throw new DirectoryNotFoundException("could not find repository root containing Library.dll");
}

static void RegisterRepositoryAssemblyResolver(string repositoryRoot)
{
    AssemblyLoadContext.Default.Resolving += (_, requestedAssembly) =>
    {
        if (string.IsNullOrWhiteSpace(requestedAssembly.Name))
            return null;
        var dependencyPath = Path.Combine(repositoryRoot, $"{requestedAssembly.Name}.dll");
        return File.Exists(dependencyPath)
            ? AssemblyLoadContext.Default.LoadFromAssemblyPath(dependencyPath)
            : null;
    };
}

static Type RequireType(Assembly assembly, string name) =>
    assembly.GetType(name, throwOnError: false)
    ?? throw new InvalidOperationException($"required type is missing: {name}");

static IEnumerable<object> ReadCollection(Type sessionType, object session, Type entityType)
{
    var getCollection = sessionType.GetMethods(BindingFlags.Instance | BindingFlags.Public)
        .SingleOrDefault(method => method.Name == "GetCollection"
            && method.IsGenericMethodDefinition
            && method.GetGenericArguments().Length == 1
            && method.GetParameters().Length == 0)
        ?? throw new InvalidOperationException("MirDB.Session.GetCollection<T>() was not found");
    var collection = getCollection.MakeGenericMethod(entityType).Invoke(session, null)
        ?? throw new InvalidOperationException($"GetCollection<{entityType.Name}> returned null");
    return collection is IEnumerable enumerable
        ? enumerable.Cast<object>()
        : throw new InvalidOperationException($"GetCollection<{entityType.Name}> did not return an enumerable collection");
}

static IEnumerable<object> ReadEnumerable(object source, string propertyName) =>
    ReadRequiredProperty(source, propertyName) is IEnumerable enumerable
        ? enumerable.Cast<object>()
        : throw new InvalidOperationException($"required field {source.GetType().FullName}.{propertyName} is not enumerable");

static object ReadRequiredProperty(object source, string propertyName)
{
    var property = source.GetType().GetProperty(propertyName, BindingFlags.Instance | BindingFlags.Public)
        ?? throw new InvalidOperationException($"required field is missing: {source.GetType().FullName}.{propertyName}");
    return property.GetValue(source)
        ?? throw new InvalidOperationException($"required field is null: {source.GetType().FullName}.{propertyName}");
}

static int ReadInt(object source, string propertyName) =>
    Convert.ToInt32(ReadRequiredProperty(source, propertyName), CultureInfo.InvariantCulture);

static bool ReadBool(object source, string propertyName) =>
    Convert.ToBoolean(ReadRequiredProperty(source, propertyName), CultureInfo.InvariantCulture);

static string ReadString(object source, string propertyName) =>
    Convert.ToString(ReadRequiredProperty(source, propertyName), CultureInfo.InvariantCulture)
    ?? throw new InvalidOperationException($"required field is not convertible to text: {source.GetType().FullName}.{propertyName}");

static string EnsureTrailingSeparator(string path) => Path.EndsInDirectorySeparator(path) ? path : path + Path.DirectorySeparatorChar;

static string ComputeSha256(string path)
{
    using var stream = File.OpenRead(path);
    return Convert.ToHexString(SHA256.HashData(stream)).ToLowerInvariant();
}

static void DeleteTemporaryDirectory(string path)
{
    if (Directory.Exists(path))
        Directory.Delete(path, recursive: true);
}

internal sealed record ExportOptions(FileInfo DatabasePath, FileInfo OutputPath);
internal sealed record ExportDocument(DatabaseSnapshot Database, List<ItemSnapshot> Items, List<MonsterSnapshot> Monsters, List<SetSnapshot> Sets);
internal sealed record DatabaseSnapshot(string Path, string Sha256, DateTimeOffset ExportedAt);
internal sealed record ItemSnapshot(int Index, string Name, string ItemType, string RequiredClass, int RequiredAmount, int Image);
internal sealed record MonsterSnapshot(int Index, string Name, int Level, int Ai, int Image, bool IsBoss);
internal sealed record SetSnapshot(int Index, string Name, List<SetGroupSnapshot> Groups);
internal sealed record SetGroupSnapshot(string Name, int RequiredNumItems, List<string> Items);
