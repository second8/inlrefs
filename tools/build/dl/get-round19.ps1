$ErrorActionPreference = "Continue"
$base = "C:\Users\38349\Desktop\01"
$items = @(
  @("N28 Atelier - Weave\round 19", "n28r19-01_editorial-sprawl-on-steps-bag-by-hip.png", "https://media.weavy.ai/image/upload/v1792429696/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/pahmlkhpgalgx3vxi3y8.png"),
  @("N28 Atelier - Weave\round 19", "n28r19-02_editorial-wall-lean-foot-on-wall-bag-at-heel.png", "https://media.weavy.ai/image/upload/v1792429697/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/gsueit1sdenla1eohs6q.png"),
  @("N31 Open Air - Weave\round 3", "n31r3-01_billboard-on-seafront-promenade-wide.png", "https://media.weavy.ai/image/upload/v1792429702/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/tpgmzfojravdofa8rfuu.png"),
  @("N31 Open Air - Weave\round 3", "n31r3-02_row-of-ad-panels-along-tram-platform-wide.png", "https://media.weavy.ai/image/upload/v1792429709/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ob70w0akqytvpbjbuuui.png"),
  @("N31 Open Air - Weave\round 3", "n31r3-03_poster-on-white-park-pavilion-lawn-wide.png", "https://media.weavy.ai/image/upload/v1792429717/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/cgni76kc0ctc4gdi634b.png"),
  @("N31 Open Air - Weave\round 3", "n31r3-04_banner-between-car-park-pillars-wide.png", "https://media.weavy.ai/image/upload/v1792429723/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/kr0bcwqtpghhirtxxjgh.png"),
  @("N31 Open Air - Weave\round 3", "n31r3-05_long-banner-on-footbridge-side-from-riverbank-wide.png", "https://media.weavy.ai/image/upload/v1792429731/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/jiszbtmhvc9kgblkkitf.png"),
  @("N31 Open Air - Weave\round 3", "n31r3-06_pair-of-lamppost-banners.png", "https://media.weavy.ai/image/upload/v1792429736/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ufwzptlzcnybu8qlyytm.png"),
  @("N31 Open Air - Weave\round 3", "n31r3-07_billboard-on-terraced-house-gable-from-back-lane.png", "https://media.weavy.ai/image/upload/v1792429755/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/mhpxthsnvwmsixvcgaxa.png"),
  @("N31 Open Air - Weave\round 3", "n31r3-08_poster-in-glass-case-museum-colonnade.png", "https://media.weavy.ai/image/upload/v1792429763/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/a3crlrvbf58ujarcx7tv.png"),
  @("N31 Open Air - Weave\round 3", "n31r3-09_tall-banner-down-stairwell-tower.png", "https://media.weavy.ai/image/upload/v1792429771/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/aw2glud8yzj2li5joygs.png"),
  @("N31 Open Air - Weave\round 3", "n31r3-10_pasted-poster-white-lane-wall-sun-stripes.png", "https://media.weavy.ai/image/upload/v1792429780/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/gt2yttaomte7hplm8obm.png")
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
