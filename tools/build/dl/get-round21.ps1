$ErrorActionPreference = "Continue"
$base = "C:\Users\38349\Desktop\01"
$items = @(
  @("N28 Atelier - Weave\round 21", "n28r21-01_bag-held-up-as-mask-hiding-face.png", "https://media.weavy.ai/image/upload/v1792431246/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/r35uobfico4rkwvpedj6.png"),
  @("N28 Atelier - Weave\round 21", "n28r21-02_clothing-box-balanced-on-head-walking-away.png", "https://media.weavy.ai/image/upload/v1792431264/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ijx6pugyfqzmvrxrii9i.png"),
  @("N28 Atelier - Weave\round 21", "n28r21-03_top-down-seated-in-grid-of-six-boxes.png", "https://media.weavy.ai/image/upload/v1792431277/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/h7b8trxqian7zhvuc64x.png"),
  @("N28 Atelier - Weave\round 21", "n28r21-04_handover-of-bag-between-two-gloved-hands.png", "https://media.weavy.ai/image/upload/v1792431289/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/vqoj6v5kyjgda1ldknjy.png"),
  @("N28 Atelier - Weave\round 21", "n28r21-05_twirl-in-shirt-dress-flash-frozen-bag.png", "https://media.weavy.ai/image/upload/v1792431308/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/abgqxlpgdmer0yqj3qi3.png"),
  @("N28 Atelier - Weave\round 21", "n28r21-06_bag-on-roof-of-black-car-gloved-hand-on-door.png", "https://media.weavy.ai/image/upload/v1792431302/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/rsfvueairvpsdv73b3hj.png"),
  @("N28 Atelier - Weave\round 21", "n28r21-07_three-identical-bags-in-row-on-steps-crossed-legs.png", "https://media.weavy.ai/image/upload/v1792431318/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/tcdetsnfcv77nzr8iqbp.png"),
  @("N28 Atelier - Weave\round 21", "n28r21-08_invitations-one-per-step-top-down-staircase.png", "https://media.weavy.ai/image/upload/v1792431328/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/pwaxnyibouqoszxvhl4v.png"),
  @("N31 Open Air - Weave\round 5", "n31r5-01_billboard-on-stilts-at-city-edge-wide.png", "https://media.weavy.ai/image/upload/v1792431332/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/aypyuwiqr8bmn1mby6vb.png"),
  @("N31 Open Air - Weave\round 5", "n31r5-02_banner-on-grandstand-back-wall-wide.png", "https://media.weavy.ai/image/upload/v1792431349/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/kufyzfrtp15dsidxl7it.png"),
  @("N31 Open Air - Weave\round 5", "n31r5-03_wallscape-on-brutalist-concrete-block-wide.png", "https://media.weavy.ai/image/upload/v1792431350/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/z4qjg1rlxs9g43xx0mme.png"),
  @("N31 Open Air - Weave\round 5", "n31r5-04_hoarding-along-canal-towpath-wide.png", "https://media.weavy.ai/image/upload/v1792431354/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ff9gqgrdh6ospqcwi2ia.png"),
  @("N31 Open Air - Weave\round 5", "n31r5-05_billboard-across-empty-car-park-wide.png", "https://media.weavy.ai/image/upload/v1792431364/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/z8fxovjheryk8cel2rxk.png"),
  @("N31 Open Air - Weave\round 5", "n31r5-06_poster-series-along-white-arcade-wide.png", "https://media.weavy.ai/image/upload/v1792431371/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/msk7e0qm1zvfi8pv4tpj.png"),
  @("N31 Open Air - Weave\round 5", "n31r5-07_gantry-billboard-over-highway-wide.png", "https://media.weavy.ai/image/upload/v1792431378/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/byu9t86yowdp6ivnhstp.png"),
  @("N31 Open Air - Weave\round 5", "n31r5-08_wallscape-on-ferry-terminal-wide.png", "https://media.weavy.ai/image/upload/v1792431384/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/mh3yy3w0zdwhdckedvf2.png"),
  @("N31 Open Air - Weave\round 5", "n31r5-09_billboard-truck-parked-on-plaza-wide.png", "https://media.weavy.ai/image/upload/v1792431391/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/iikuf9vtuqmzjzfmelkk.png"),
  @("N31 Open Air - Weave\round 5", "n31r5-10_long-poster-under-concrete-pergola-wide.png", "https://media.weavy.ai/image/upload/v1792431399/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/xueyuswlnh135zuwmwth.png"),
  @("N31 Open Air - Weave\round 5", "n31r5-11_poster-on-kiosk-side-panel.png", "https://media.weavy.ai/image/upload/v1792431407/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/lmd6ykpjedtri49a5ed6.png"),
  @("N31 Open Air - Weave\round 5", "n31r5-12_rooftop-billboard-through-gap-between-buildings.png", "https://media.weavy.ai/image/upload/v1792431413/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/nekmu2hc92glxigqf8uf.png"),
  @("N31 Open Air - Weave\round 5", "n31r5-13_banner-on-construction-lift-tower.png", "https://media.weavy.ai/image/upload/v1792431422/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/b4ud3zmn6zeb0fjanb64.png"),
  @("N31 Open Air - Weave\round 5", "n31r5-14_poster-in-ferry-pier-shelter.png", "https://media.weavy.ai/image/upload/v1792431432/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/rwzxpwnb3slmgv13f0wu.png"),
  @("N31 Open Air - Weave\round 5", "n31r5-15_freestanding-poster-frame-on-boardwalk.png", "https://media.weavy.ai/image/upload/v1792431436/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/cfvdq730raz3v2atbc3n.png"),
  @("N31 Open Air - Weave\round 5", "n31r5-16_vertical-wallscape-on-narrow-townhouse.png", "https://media.weavy.ai/image/upload/v1792431443/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/u45znxlgxvl5xrxfq63e.png"),
  @("N31 Open Air - Weave\round 5", "n31r5-17_poster-in-stone-wall-niche.png", "https://media.weavy.ai/image/upload/v1792431451/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ms9d6mmowdhdinmasfmu.png"),
  @("N31 Open Air - Weave\round 5", "n31r5-18_rooftop-billboard-from-high-balcony.png", "https://media.weavy.ai/image/upload/v1792431466/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ilg46flbjsocxfwmdb6q.png"),
  @("N31 Open Air - Weave\round 5", "n31r5-19_vertical-banner-on-sports-hall-facade.png", "https://media.weavy.ai/image/upload/v1792431466/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/sokqlbgszufsaf99eq7j.png"),
  @("N31 Open Air - Weave\round 5", "n31r5-20_poster-on-pale-blue-garage-door.png", "https://media.weavy.ai/image/upload/v1792431476/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/tl1nfnp6da9yxtlny4ar.png")
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
