# CCBP / ASP Bootstrap Installer
# Default state: DISABLED (explicit sign-enable required)

Write-Host "Bootstrapping governance tools..."

# Ensure repo root
if (-not (Test-Path ".git")) {
    throw "Not at repo root (no .git directory found)."
}

# Create directories
New-Item -ItemType Directory -Path .ccbp -ErrorAction SilentlyContinue | Out-Null
New-Item -ItemType Directory -Path tools -ErrorAction SilentlyContinue | Out-Null

# Disable by default
$enablePath = ".ccbp/SIGN_ENABLE"
if (-not (Test-Path $enablePath)) {
    New-Item -ItemType File -Path $enablePath | Out-Null
    Write-Host "Governance state: DISABLED"
}

# Install tool if missing
$toolPath = ".\tools\ccbp.ps1"
if (-not (Test-Path $toolPath)) {
    throw "ccbp.ps1 not found. Copy tool into tools/ before bootstrap."
}

Write-Host "Bootstrap complete."
Write-Host "Run: .\tools\ccbp.ps1 enable  (explicit authority required)"
