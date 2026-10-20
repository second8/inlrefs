$ErrorActionPreference = "Continue"
$base = "C:\Users\38349\Desktop\01"
$items = @(
  @("N32 Restaurant - Weave\round 5", "n32r5-01_gold-rimmed-dinner-plate-centre-set-table-top-down.png", "https://media.weavy.ai/image/upload/v1792498391/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/hfvlaxsfjd7hz6zq8ecj.png"),
  @("N32 Restaurant - Weave\round 5", "n32r5-02_brass-framed-plaque-white-marble-wall-by-glass-door.png", "https://media.weavy.ai/image/upload/v1792498401/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/yhvwy4whrzwe5ivcxrn9.png"),
  @("N32 Restaurant - Weave\round 5", "n32r5-03_frosted-glass-door-panel-dusk-street-reflections.png", "https://media.weavy.ai/image/upload/v1792498403/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/aic35u3gmhjstljewzz1.png"),
  @("N32 Restaurant - Weave\round 5", "n32r5-04_luxury-shopping-bag-bronze-bar-champagne.png", "https://media.weavy.ai/image/upload/v1792498418/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ycsmlm7fzytb1eniwh7j.png"),
  @("N32 Restaurant - Weave\round 5", "n32r5-05_host-stand-ipad-bronze-stand-white-flowers.png", "https://media.weavy.ai/image/upload/v1792498426/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/elhr6revpfzyqorzxl3z.png"),
  @("N32 Restaurant - Weave\round 5", "n32r5-06_tall-menu-board-bronze-easel-entrance-candlelight.png", "https://media.weavy.ai/image/upload/v1792498430/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/y9ohq3n4ru0kclpckl1e.png")
)
$ok=0; $have=0; $fail=0
foreach ($it in $items) {
  $dir = Join-Path $base $it[0]
  New-Item -ItemType Directory -Force -Path $dir | Out-Null
  $dst = Join-Path $dir $it[1]
  if (Test-Path $dst) { $have++; continue }
  $done=$false
  for ($i=1; $i -le 3 -and -not $done; $i++) {
    try { Invoke-WebRequest -Uri $it[2] -OutFile $dst -UseBasicParsing; $done=$true; $ok++ }
    catch { Start-Sleep -Seconds 2 }
  }
  if (-not $done) { $fail++; Write-Host "Failed: $($it[1])" }
}
Write-Host "Done. $ok images, $have already there, $fail failed."
