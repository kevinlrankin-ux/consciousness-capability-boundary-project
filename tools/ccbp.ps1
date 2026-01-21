param(
  [ValidateSet("status","enable","disable","apply-oh01","commit-push")]
  [string]$Cmd = "status",
  [string]$Message = ""
)

$RepoRoot = (git rev-parse --show-toplevel 2>$null)
if (-not $RepoRoot) { throw "Not in a git repo." }
Set-Location $RepoRoot

$GatePath = Join-Path $RepoRoot ".ccbp\SIGN_ENABLE"

function Require-Enabled {
  if (-not (Test-Path $GatePath)) {
    throw "AUTOMATION DISABLED. Create .ccbp\SIGN_ENABLE (run: .\tools\ccbp.ps1 enable) to proceed."
  }
}

switch ($Cmd) {

  "status" {
    $enabled = Test-Path $GatePath
    Write-Host ("Repo: " + $RepoRoot)
    Write-Host ("Automation: " + ($(if($enabled){"ENABLED"}else{"DISABLED"})))
    git status
  }

  "enable" {
    New-Item -ItemType File -Force -Path $GatePath | Out-Null
    Write-Host "Automation ENABLED (SIGN_ENABLE present)."
  }

  "disable" {
    if (Test-Path $GatePath) { Remove-Item $GatePath -Force }
    Write-Host "Automation DISABLED (SIGN_ENABLE removed)."
  }

  "apply-oh01" {
    Require-Enabled

    $path = ".\protocols\oh-01-orientation-handshake.md"
    if (-not (Test-Path $path)) { throw "Missing: $path" }

    $content = Get-Content $path -Raw
    if ($content.Trim().Length -gt 0) { throw "Refusing: OH-01 file is not empty. (Prevents accidental overwrite.)" }

    $block = @"
# OH-01 — Orientation Handshake (Validator Layer)

## Status
This document is **authoritative** as a *validator/spec layer* artifact under the Consciousness–Capability Boundary Project (CCBP).
It does **not** modify Book I or Book II; it operationalizes an *orientation check* using what systems already provide: an answer to “who am I”.

## Purpose
Detect **mimicry** by requiring a minimal, identity-anchored, context-bound “orientation response” that a legitimate system can produce reliably,
but a copier cannot reproduce without possessing the same authority posture, provenance bindings, and operational context.

## Core Requirement (Non-Directive)
Implementations MAY perform an Orientation Handshake, but if claimed, they MUST:
1) Bind the response to the system’s own identity surface (process/runtime/app instance identity).
2) Bind the response to the active context (time window + session + declared mode).
3) Bind the response to declared provenance (repository + version/commit or equivalent).
4) Produce a deterministic “orientation transcript” suitable for audit (no hidden steps claimed as proof).

## Output Contract
An OH-01 transcript MUST include:
- Declared identity surface (what the system claims it is)
- Declared context (what situation it is in)
- Declared provenance (what definitions/specs it is operating under)
- Declared constraints (what it will not do)
- A verifier result: PASS/FAIL + reason code(s)

## Notes
OH-01 is intended to reduce successful “Envelope mimicry” without introducing new axioms into Book I/II.
Optional stronger binding (polymer + on-chain linkage) can be layered for high-sensitivity operations.
"@

    Set-Content -Path $path -Value $block -Encoding UTF8
    Write-Host "OH-01 block inserted."
  }

  "commit-push" {
    Require-Enabled

    if (-not $Message) { throw "Provide -Message for commit-push." }
    git add -A
    git commit -m $Message
    git push origin main
  }
}
