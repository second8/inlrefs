$ErrorActionPreference = "Continue"
$base = "C:\Users\38349\Desktop\01"
$items = @(
  @("N31 Open Air - Weave\round 7", "n31r7-01_wallscape-mirrored-in-warehouse-yard-puddle-wide.png", "https://media.weavy.ai/image/upload/v1792486433/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/akurxe7rulikbzm7kml5.png"),
  @("N31 Open Air - Weave\round 7", "n31r7-02_billboard-mirrored-in-still-canal-wide.png", "https://media.weavy.ai/image/upload/v1792486441/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ufu2314f8rtlmhyo159r.png"),
  @("N31 Open Air - Weave\round 7", "n31r7-03_rooftop-billboard-mirrored-in-granite-reflecting-pool-wide.png", "https://media.weavy.ai/image/upload/v1792486450/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/qucvxasw53nyayfhqpnr.png"),
  @("N31 Open Air - Weave\round 7", "n31r7-04_banner-on-lakeside-pavilion-mirrored-in-lake-wide.png", "https://media.weavy.ai/image/upload/v1792486455/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ojhtwfumeht6leozpwv3.png"),
  @("N31 Open Air - Weave\round 7", "n31r7-05_billboard-through-circular-lobby-window-wide.png", "https://media.weavy.ai/image/upload/v1792486462/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/eiavvfhnd813nsqkbatt.png"),
  @("N31 Open Air - Weave\round 7", "n31r7-06_billboard-framed-by-two-identical-white-vans-wide.png", "https://media.weavy.ai/image/upload/v1792486476/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/wk0mew2yk3ta2brhkzuy.png"),
  @("N31 Open Air - Weave\round 7", "n31r7-07_billboard-above-row-of-striped-beach-umbrellas-wide.png", "https://media.weavy.ai/image/upload/v1792486481/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/y4dsgbpvpwdniqzlm7uk.png"),
  @("N31 Open Air - Weave\round 7", "n31r7-08_basketball-player-mid-jump-below-billboard-wide.png", "https://media.weavy.ai/image/upload/v1792486498/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/hqlpvfpeqdgyrcts45gv.png"),
  @("N31 Open Air - Weave\round 7", "n31r7-09_billboard-from-inside-cable-car-wide.png", "https://media.weavy.ai/image/upload/v1792486499/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/zmpdcuoqqcvzzbhc5vbr.png"),
  @("N31 Open Air - Weave\round 7", "n31r7-10_billboard-at-end-of-straight-railway-line-wide.png", "https://media.weavy.ai/image/upload/v1792486502/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/u0c87evp4tqojy0r4y2j.png"),
  @("N31 Open Air - Weave\round 7", "n31r7-11_wallscape-on-wall-of-stacked-white-containers-wide.png", "https://media.weavy.ai/image/upload/v1792486514/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/aj0qjtx8mqb5vbxqbvai.png"),
  @("N31 Open Air - Weave\round 7", "n31r7-12_billboard-from-kayak-bow-at-water-level-wide.png", "https://media.weavy.ai/image/upload/v1792486522/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/b8jkrrut5qnyduef3ugb.png"),
  @("N31 Open Air - Weave\round 7", "n31r7-13_underpass-poster-shaft-of-sun-cyclist-wide.png", "https://media.weavy.ai/image/upload/v1792486530/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/utymbrmvzzxpvf5daphz.png"),
  @("N31 Open Air - Weave\round 7", "n31r7-14_billboard-over-terraced-vineyard-wide.png", "https://media.weavy.ai/image/upload/v1792486541/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/yrkhufiimpwl5gqlqxa5.png"),
  @("N31 Open Air - Weave\round 7", "n31r7-15_billboard-between-two-sheets-on-rooftop-washing-line-wide.png", "https://media.weavy.ai/image/upload/v1792486547/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/wx6swcgxwlw1ooowmiad.png"),
  @("N31 Open Air - Weave\round 7", "n31r7-16_billboard-across-stadium-track-sprinter-blurred-wide.png", "https://media.weavy.ai/image/upload/v1792486555/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/xg4c5k5v3wphymsj0ok2.png"),
  @("N31 Open Air - Weave\round 7", "n31r7-17_billboard-above-row-of-pastel-beach-huts-wide.png", "https://media.weavy.ai/image/upload/v1792486568/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/x6bjbkcm2pesy3owtrna.png"),
  @("N31 Open Air - Weave\round 7", "n31r7-18_billboard-across-rooftop-of-solar-panels-wide.png", "https://media.weavy.ai/image/upload/v1792486571/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/msdxzcy3a0fau54w7iki.png"),
  @("N31 Open Air - Weave\round 7", "n31r7-19_billboard-through-gap-in-row-of-cypresses-wide.png", "https://media.weavy.ai/image/upload/v1792486584/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/faatwge1v0wrpzhvfbah.png"),
  @("N31 Open Air - Weave\round 7", "n31r7-20_billboard-with-plane-contrail-high-above-wide.png", "https://media.weavy.ai/image/upload/v1792486582/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/x6apr6nsywy7vkxrn1sl.png")
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
