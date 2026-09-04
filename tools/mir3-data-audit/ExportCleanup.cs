namespace Mir3DataAudit;

public static class ExportCleanup
{
    public const string FailureDataKey = "Mir3DataAudit.CleanupFailure";

    public static void Run(Exception? exportFailure, params Action[] operations)
    {
        var failures = new List<Exception>();
        foreach (var operation in operations)
        {
            try
            {
                operation();
            }
            catch (Exception exception)
            {
                failures.Add(exception);
            }
        }

        if (failures.Count == 0)
            return;

        var cleanupFailure = failures.Count == 1
            ? failures[0]
            : new AggregateException("multiple temporary cleanup operations failed", failures);
        if (exportFailure is not null)
        {
            exportFailure.Data[FailureDataKey] = cleanupFailure;
            return;
        }

        var cleanupException = new InvalidOperationException("export cleanup failed", cleanupFailure);
        cleanupException.Data[FailureDataKey] = cleanupFailure;
        throw cleanupException;
    }
}
