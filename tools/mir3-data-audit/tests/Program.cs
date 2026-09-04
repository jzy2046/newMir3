using Mir3DataAudit;

DatabaseHashBinding.RequireMatch("same", "same", "same");
ExpectFailure(() => DatabaseHashBinding.RequireMatch("before", "after", "before"));
ExpectFailure(() => DatabaseHashBinding.RequireMatch("same", "same", "copy"));

var attempts = new List<string>();
var originalFailure = new InvalidOperationException("original export failure");
ExportCleanup.Run(originalFailure,
    () => { attempts.Add("session"); throw new IOException("session cleanup failure"); },
    () => { attempts.Add("database"); throw new IOException("database cleanup failure"); },
    () => { attempts.Add("backup"); throw new IOException("backup cleanup failure"); });
if (!attempts.SequenceEqual(new[] { "session", "database", "backup" }))
    throw new InvalidOperationException("cleanup stopped before all operations were attempted");
if (originalFailure.Data[ExportCleanup.FailureDataKey] is not AggregateException { InnerExceptions.Count: 3 })
    throw new InvalidOperationException("cleanup failures were not attached to the original export failure");

attempts.Clear();
try
{
    ExportCleanup.Run(null,
        () => { attempts.Add("session"); throw new IOException("session cleanup failure"); },
        () => attempts.Add("database"),
        () => { attempts.Add("backup"); throw new IOException("backup cleanup failure"); });
    throw new InvalidOperationException("cleanup-only failure was not reported");
}
catch (InvalidOperationException exception) when (exception.Message == "export cleanup failed")
{
    if (exception.InnerException is not AggregateException { InnerExceptions.Count: 2 })
        throw new InvalidOperationException("cleanup-only failures were not preserved", exception);
}
if (!attempts.SequenceEqual(new[] { "session", "database", "backup" }))
    throw new InvalidOperationException("cleanup-only failure stopped later cleanup operations");
Console.WriteLine("hash binding regression checks passed");

static void ExpectFailure(Action action)
{
    try
    {
        action();
    }
    catch (InvalidOperationException)
    {
        return;
    }

    throw new InvalidOperationException("hash mismatch was accepted");
}
