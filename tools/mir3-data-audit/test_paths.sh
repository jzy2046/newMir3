#!/usr/bin/env bash
set -euo pipefail

repository_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
dotnet_command="${DOTNET_COMMAND:-}"
if [[ -z "$dotnet_command" ]]; then
    dotnet_command="$(command -v dotnet || true)"
fi
if [[ -z "$dotnet_command" ]]; then
    echo "DOTNET_COMMAND is not set and dotnet is not on PATH" >&2
    exit 1
fi
temporary_root="$(mktemp -d "${TMPDIR:-/tmp}/mir3-data-audit-paths.XXXXXX")"
trap 'rm -rf "$temporary_root"' EXIT

failures=0

"$dotnet_command" build "$repository_root/tools/mir3-data-audit/Mir3DataAudit.csproj" --nologo >/dev/null

expect_rejected_without_database_change() {
    local label="$1"
    local database_argument="$2"
    local output_argument="$3"
    local copied_database="$4"
    local before_sha after_sha exit_code

    before_sha="$(shasum -a 256 "$copied_database" | awk '{print $1}')"
    set +e
    "$dotnet_command" run --project "$repository_root/tools/mir3-data-audit/Mir3DataAudit.csproj" -- \
        export --database "$database_argument" --output "$output_argument"
    exit_code=$?
    set -e
    after_sha="$(shasum -a 256 "$copied_database" | awk '{print $1}')"

    if [[ "$exit_code" -eq 0 ]]; then
        echo "FAIL: $label was accepted" >&2
        failures=$((failures + 1))
    fi
    if [[ "$before_sha" != "$after_sha" ]]; then
        echo "FAIL: $label changed the copied database" >&2
        failures=$((failures + 1))
    fi
}

cp "$repository_root/Database/System.db" "$temporary_root/System.db"
expect_rejected_without_database_change \
    "database and output resolving to the same file" \
    "$temporary_root/System.db" \
    "$temporary_root/System.db" \
    "$temporary_root/System.db"

mkdir "$temporary_root/symlink"
cp "$repository_root/Database/System.db" "$temporary_root/symlink/System.db"
ln -s "$temporary_root/symlink/System.db" "$temporary_root/system-link.json"
expect_rejected_without_database_change \
    "output symlink resolving to the input database" \
    "$temporary_root/symlink/System.db" \
    "$temporary_root/system-link.json" \
    "$temporary_root/symlink/System.db"

mkdir "$temporary_root/hardlink"
cp "$repository_root/Database/System.db" "$temporary_root/hardlink/System.db"
ln "$temporary_root/hardlink/System.db" "$temporary_root/hardlink-output.json"
expect_rejected_without_database_change \
    "output hard link resolving to the input database" \
    "$temporary_root/hardlink/System.db" \
    "$temporary_root/hardlink-output.json" \
    "$temporary_root/hardlink/System.db"

mkdir "$temporary_root/parent-target"
cp "$repository_root/Database/System.db" "$temporary_root/parent-target/System.db"
ln -s "$temporary_root/parent-target" "$temporary_root/parent-link"
expect_rejected_without_database_change \
    "output through a parent-directory symlink" \
    "$temporary_root/parent-target/System.db" \
    "$temporary_root/parent-link/System.db" \
    "$temporary_root/parent-target/System.db"

mkdir "$temporary_root/ordinary-existing"
cp "$repository_root/Database/System.db" "$temporary_root/ordinary-existing/System.db"
printf 'already exists\n' > "$temporary_root/ordinary-existing-output.json"
expect_rejected_without_database_change \
    "ordinary existing output file" \
    "$temporary_root/ordinary-existing/System.db" \
    "$temporary_root/ordinary-existing-output.json" \
    "$temporary_root/ordinary-existing/System.db"

mkdir "$temporary_root/relative"
cp "$repository_root/Database/System.db" "$temporary_root/relative/System.db"
pushd "$temporary_root/relative" >/dev/null
expect_rejected_without_database_change \
    "relative database path" \
    "System.db" \
    "$temporary_root/relative-output.json" \
    "$temporary_root/relative/System.db"
popd >/dev/null

cp "$repository_root/Database/System.db" "$temporary_root/NotSystem.db"
expect_rejected_without_database_change \
    "non-exact System.db filename" \
    "$temporary_root/NotSystem.db" \
    "$temporary_root/not-system-output.json" \
    "$temporary_root/NotSystem.db"

mkdir "$temporary_root/new-output"
cp "$repository_root/Database/System.db" "$temporary_root/new-output/System.db"
before_sha="$(shasum -a 256 "$temporary_root/new-output/System.db" | awk '{print $1}')"
"$dotnet_command" run --project "$repository_root/tools/mir3-data-audit/Mir3DataAudit.csproj" -- \
    export --database "$temporary_root/new-output/System.db" --output "$temporary_root/new-output/current-system.json"
after_sha="$(shasum -a 256 "$temporary_root/new-output/System.db" | awk '{print $1}')"
if [[ "$before_sha" != "$after_sha" || ! -f "$temporary_root/new-output/current-system.json" ]]; then
    echo "FAIL: new output export did not preserve the copied database" >&2
    failures=$((failures + 1))
fi
if [[ "$(python3 -c 'import json, sys; print(json.load(open(sys.argv[1], encoding="utf-8"))["database"]["path"])' "$temporary_root/new-output/current-system.json")" != "Database/System.db" ]]; then
    echo "FAIL: snapshot database.path is not stable" >&2
    failures=$((failures + 1))
fi
snapshot_sha="$(python3 -c 'import json, sys; print(json.load(open(sys.argv[1], encoding="utf-8"))["database"]["sha256"])' "$temporary_root/new-output/current-system.json")"
if [[ "$snapshot_sha" != "$before_sha" ]]; then
    echo "FAIL: snapshot SHA-256 is not bound to the verified database copy" >&2
    failures=$((failures + 1))
fi

if [[ "$failures" -ne 0 ]]; then
    exit 1
fi

echo "path validation regression checks passed"
