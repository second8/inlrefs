$ErrorActionPreference = "Continue"
$base = "C:\Users\38349\Desktop\01"
$items = @(
  @("N33 Devices - Weave\round 2", "n33r2-01_machined-control-unit-knurled-dials-tick-scales.png", "https://media.weavy.ai/image/upload/v1792499524/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/fh6ljznif4iatkpgcz0y.png"),
  @("N33 Devices - Weave\round 2", "n33r2-02_ev-charger-steel-cap-glass-face-docked-handle.png", "https://media.weavy.ai/image/upload/v1792499314/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/zxqs4egqv3ot2o5blucn.png"),
  @("N33 Devices - Weave\round 2", "n33r2-03_soft-touch-handheld-chunky-icon-buttons.png", "https://media.weavy.ai/image/upload/v1792499317/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ujaihsdmp6doy9et83b1.png"),
  @("N33 Devices - Weave\round 2", "n33r2-04_anodised-slab-device-encoder-switches-top-down.png", "https://media.weavy.ai/image/upload/v1792499327/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/extuwe7tqljokmevenni.png"),
  @("N33 Devices - Weave\round 2", "n33r2-05_premium-camera-rear-screen-knurled-dials.png", "https://media.weavy.ai/image/upload/v1792499334/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/xn3nl7uiavfiiwrjwnp8.png")
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
