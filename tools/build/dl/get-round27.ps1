$ErrorActionPreference = "Continue"
$base = "C:\Users\38349\Desktop\01"
$items = @(
  @("N32 Restaurant - Weave\round 4", "n32r4-01_menu-card-marble-silver-champagne-bucket-two-flutes.png", "https://media.weavy.ai/image/upload/v1792496838/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/qwn3jyfijh2qgmmfv9vj.png"),
  @("N32 Restaurant - Weave\round 4", "n32r4-02_coaster-bronze-pink-champagne-coupe-raspberry.png", "https://media.weavy.ai/image/upload/v1792496845/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ie7e1315oe9mh0zc823b.png"),
  @("N32 Restaurant - Weave\round 4", "n32r4-03_place-card-white-cloth-espresso-gold-rim-truffles.png", "https://media.weavy.ai/image/upload/v1792496845/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/bumczbhyv32tmdzbvrn4.png"),
  @("N32 Restaurant - Weave\round 4", "n32r4-04_menu-in-silver-holder-white-orchid-stems.png", "https://media.weavy.ai/image/upload/v1792496858/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/jplp7e3uyi3cnrkxby4n.png"),
  @("N32 Restaurant - Weave\round 4", "n32r4-05_tasting-menu-ivory-linen-seared-scallops-gold-rim.png", "https://media.weavy.ai/image/upload/v1792497047/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/knuzzd5vohtnmjoyqnku.png"),
  @("N32 Restaurant - Weave\round 4", "n32r4-06_business-card-marble-silver-ice-bucket-two-tumblers.png", "https://media.weavy.ai/image/upload/v1792496882/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/vcjagczhx1lpizwkkn2z.png"),
  @("N32 Restaurant - Weave\round 4", "n32r4-07_hand-placing-reservation-card-white-roses-crystal-vase.png", "https://media.weavy.ai/image/upload/v1792496887/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/p2sx70yt0clmdrku5wbk.png"),
  @("N32 Restaurant - Weave\round 4", "n32r4-08_gift-card-white-box-ivory-tissue-bronze-ribbon.png", "https://media.weavy.ai/image/upload/v1792496889/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/pxrgnvgguyiychiwmzxp.png"),
  @("N32 Restaurant - Weave\round 4", "n32r4-09_coaster-marble-tongs-placing-clear-ice-crystal-glass.png", "https://media.weavy.ai/image/upload/v1792496900/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/qi1mhukpqqb8jm49o254.png"),
  @("N32 Restaurant - Weave\round 4", "n32r4-10_menu-card-white-cloth-lobster-silver-platter.png", "https://media.weavy.ai/image/upload/v1792496907/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/gid22pouyysstppd9yed.png"),
  @("N32 Restaurant - Weave\round 4", "n32r4-11_folded-card-bronze-bar-pour-from-silver-shaker.png", "https://media.weavy.ai/image/upload/v1792496925/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/y5ds2hlue8wa1jp2pdcq.png"),
  @("N32 Restaurant - Weave\round 4", "n32r4-12_dessert-card-marble-silver-tier-petits-fours.png", "https://media.weavy.ai/image/upload/v1792496930/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/d8ipswgefyrnyvkmsx13.png"),
  @("N32 Restaurant - Weave\round 4", "n32r4-13_napkin-band-gold-rim-plate-crystal-silver-symmetric.png", "https://media.weavy.ai/image/upload/v1792496935/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/aibkiudwxye8domxemp5.png"),
  @("N32 Restaurant - Weave\round 4", "n32r4-14_card-white-cloth-night-crystal-votives-red-wine.png", "https://media.weavy.ai/image/upload/v1792496941/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ixgzx4jiaoamqhcbrj1w.png"),
  @("N32 Restaurant - Weave\round 4", "n32r4-15_wine-list-white-cloth-two-hands-toasting-flutes.png", "https://media.weavy.ai/image/upload/v1792496947/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/nvirluko2r6ievs7mnxx.png")
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
