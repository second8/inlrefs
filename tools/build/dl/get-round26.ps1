$ErrorActionPreference = "Continue"
$base = "C:\Users\38349\Desktop\01"
$items = @(
  @("N32 Restaurant - Weave\round 3", "n32r3-01_menu-card-white-cloth-caviar-tin-on-ice-full-coupe.png", "https://media.weavy.ai/image/upload/v1792491904/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/tjhookxl7hf9bkpehazc.png"),
  @("N32 Restaurant - Weave\round 3", "n32r3-02_coaster-marble-bar-hand-pouring-champagne-coupe.png", "https://media.weavy.ai/image/upload/v1792491845/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/zqtyx0olodcpdhgbekzn.png"),
  @("N32 Restaurant - Weave\round 3", "n32r3-03_wine-list-white-cloth-sommelier-pouring-red.png", "https://media.weavy.ai/image/upload/v1792491915/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/dlfaj9tmwgs3uxvijuyq.png"),
  @("N32 Restaurant - Weave\round 3", "n32r3-04_place-card-full-fine-dining-setting-ivory-linen.png", "https://media.weavy.ai/image/upload/v1792491856/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/qi8nycqms3tt5atvm8ck.png"),
  @("N32 Restaurant - Weave\round 3", "n32r3-05_menu-card-marble-silver-tray-oysters-on-ice.png", "https://media.weavy.ai/image/upload/v1792491872/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/h0nbxsfuvy1foj40d547.png"),
  @("N32 Restaurant - Weave\round 3", "n32r3-06_business-card-bronze-crystal-decanter-cognac.png", "https://media.weavy.ai/image/upload/v1792491877/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/cwdzxdyxqflfs6zufzuu.png"),
  @("N32 Restaurant - Weave\round 3", "n32r3-07_tasting-menu-white-cloth-silver-candelabra-night.png", "https://media.weavy.ai/image/upload/v1792491884/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/elob9kmv15ouxzocpi1z.png"),
  @("N32 Restaurant - Weave\round 3", "n32r3-08_invitation-card-envelope-marble-white-rose-flute.png", "https://media.weavy.ai/image/upload/v1792491894/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/jj34i7etknxtsprg9fti.png"),
  @("N32 Restaurant - Weave\round 3", "n32r3-09_folded-card-bronze-bar-champagne-coupe-tower.png", "https://media.weavy.ai/image/upload/v1792491900/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/pb4fixm8shomsmwfjbg5.png"),
  @("N32 Restaurant - Weave\round 3", "n32r3-10_dessert-menu-marble-gold-leaf-dessert-fine-china.png", "https://media.weavy.ai/image/upload/v1792491917/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ix9bl4tbeaha5mikusuw.png"),
  @("N32 Restaurant - Weave\round 3", "n32r3-11_coaster-bronze-whisky-ice-sphere-silver-jigger.png", "https://media.weavy.ai/image/upload/v1792491920/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/aibxym5fhnbaybwaxpmb.png"),
  @("N32 Restaurant - Weave\round 3", "n32r3-12_hand-with-gold-ring-holding-menu-over-white-cloth.png", "https://media.weavy.ai/image/upload/v1792491928/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/fsyullt2vevih0lb6sbw.png"),
  @("N32 Restaurant - Weave\round 3", "n32r3-13_table-number-long-banquet-candles-white-peonies.png", "https://media.weavy.ai/image/upload/v1792491938/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ie2trbowxey8we4jhzha.png"),
  @("N32 Restaurant - Weave\round 3", "n32r3-14_reservation-card-marble-hand-lifting-silver-cloche.png", "https://media.weavy.ai/image/upload/v1792491943/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/e6rmfzgbortdss97vo0h.png"),
  @("N32 Restaurant - Weave\round 3", "n32r3-15_menu-on-gold-rimmed-charger-folded-napkin-crystal.png", "https://media.weavy.ai/image/upload/v1792491953/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/n3mx7y3jmuh2vp1wwbkz.png")
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
