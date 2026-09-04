namespace Mir3DataAudit;

public static class DatabaseHashBinding
{
    public static void RequireMatch(string sourceBeforeCopy, string sourceAfterCopy, string copiedDatabase)
    {
        if (string.Equals(sourceBeforeCopy, sourceAfterCopy, StringComparison.Ordinal)
            && string.Equals(sourceBeforeCopy, copiedDatabase, StringComparison.Ordinal))
            return;

        throw new InvalidOperationException(
            "System.db changed during copy or the temporary copy does not match the source "
            + $"(before={sourceBeforeCopy}, after={sourceAfterCopy}, copy={copiedDatabase})");
    }
}
