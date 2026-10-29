param([Parameter(Mandatory=$true)][string]$Baseline)
$ErrorActionPreference = 'Stop'
python scripts/check_integrations.py --root . --config config/integrations.json --baseline $Baseline
if ($LASTEXITCODE -ne 0) { throw 'Integration or baseline check failed; publish stopped.' }
git diff --check
if ($LASTEXITCODE -ne 0) { throw 'Diff validation failed; publish stopped.' }
git push origin main
if ($LASTEXITCODE -ne 0) { throw 'Push failed.' }
