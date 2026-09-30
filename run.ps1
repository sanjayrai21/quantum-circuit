param(
    [string]$Target
)

if ($Target) {
    uv run python "$PSScriptRoot/run.py" $Target
} else {
    uv run python "$PSScriptRoot/run.py"
}
