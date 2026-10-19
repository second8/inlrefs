$ErrorActionPreference = "Continue"
$base = "C:\Users\38349\Desktop\01"
$items = @(
  @("N28 Atelier - Weave\round 8", "n28r8-01_bag-carried-side-crop-on-black.png", "https://media.weavy.ai/image/upload/v1792414760/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/twedhtqgu9lbvhm1tvls.png"),
  @("N28 Atelier - Weave\round 8", "n28r8-02_hang-tag-on-coat-on-rail-hard-slash.png", "https://media.weavy.ai/image/upload/v1792414761/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/atxng9ebvnjyemwhxwhx.png"),
  @("N28 Atelier - Weave\round 8", "n28r8-03_shirt-dress-on-hanger-tag-at-collar.png", "https://media.weavy.ai/image/upload/v1792414769/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/t25nfavyfcqqv9jjg6m1.png"),
  @("N28 Atelier - Weave\round 8", "n28r8-04_invitation-tucked-in-tissue-top-down.png", "https://media.weavy.ai/image/upload/v1792414778/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ep7mlfdt9mdeapbxvzsx.png"),
  @("N28 Atelier - Weave\round 8", "n28r8-05_invitation-past-fluted-glass-studio.png", "https://media.weavy.ai/image/upload/v1792414790/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ntvyufrpvg2p60grajcz.png"),
  @("N29 Spatial - Weave\round 1", "n29r1-01_monumental-lightbox-dark-hall.png", "https://media.weavy.ai/image/upload/v1792414793/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/jf4hw9pyvhvoxc4nuynr.png"),
  @("N29 Spatial - Weave\round 1", "n29r1-02_lightbox-in-snowfield-blue-hour.png", "https://media.weavy.ai/image/upload/v1792414803/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/lfxlx878fvjcd6a5qj2s.png"),
  @("N29 Spatial - Weave\round 1", "n29r1-03_one-lit-crt-before-stacked-dark-crts.png", "https://media.weavy.ai/image/upload/v1792414814/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/xiut6v8if1ypq2ncgl4g.png"),
  @("N29 Spatial - Weave\round 1", "n29r1-04_flat-screen-on-white-gallery-floor.png", "https://media.weavy.ai/image/upload/v1792414827/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/enxj6zar6qrh37y3ldro.png"),
  @("N29 Spatial - Weave\round 1", "n29r1-05_projection-wall-dark-room-silhouettes.png", "https://media.weavy.ai/image/upload/v1792414827/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/l3h7l6vtaecipue8lopw.png"),
  @("N30 Low Cloud - Weave\round 1", "n30r1-01_led-tower-wet-plaza-skyline-in-cloud.png", "https://media.weavy.ai/image/upload/v1792414833/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/x8zlsdc6pfkejbndlff0.png"),
  @("N30 Low Cloud - Weave\round 1", "n30r1-02_wide-screen-on-plinth-smog-square.png", "https://media.weavy.ai/image/upload/v1792414846/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/jhdwsmvp08cbo9iv5lwh.png"),
  @("N30 Low Cloud - Weave\round 1", "n30r1-03_lit-billboard-night-low-cloud.png", "https://media.weavy.ai/image/upload/v1792414850/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/yvztwe4qexkypfomxlgk.png"),
  @("N30 Low Cloud - Weave\round 1", "n30r1-04_bus-shelter-lightbox-fog-night.png", "https://media.weavy.ai/image/upload/v1792414859/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/qwjihtawg5nm4pwa3mnw.png"),
  @("N30 Low Cloud - Weave\round 1", "n30r1-05_phone-in-hand-on-bridge-city-in-cloud.png", "https://media.weavy.ai/image/upload/v1792414876/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/kytkov83ywnzdmj1dqsw.png")
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
