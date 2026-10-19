$ErrorActionPreference = "Continue"
$base = "C:\Users\38349\Desktop\01"
$items = @(
  @("N28 Atelier - Weave\round 15", "n28r15-01_neck-label-inside-coat-laid-flat-top-down.png", "https://media.weavy.ai/image/upload/v1792423497/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/bhi6oopdxw652bwelg19.png"),
  @("N28 Atelier - Weave\round 15", "n28r15-02_shoe-box-on-pavement-by-boots-top-down.png", "https://media.weavy.ai/image/upload/v1792423515/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/iqeywuw8swvvm152wcqe.png"),
  @("N28 Atelier - Weave\round 15", "n28r15-03_blade-sign-on-brass-bracket-above-door.png", "https://media.weavy.ai/image/upload/v1792423515/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/acwdfszstyas6orhjkky.png"),
  @("N28 Atelier - Weave\round 15", "n28r15-04_silk-scarf-laid-flat-on-stone-ledge-top-down.png", "https://media.weavy.ai/image/upload/v1792423520/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/zvprvwxzv7h3hevnyncc.png"),
  @("N28 Atelier - Weave\round 15", "n28r15-05_clothing-box-under-arm-mid-stride-side-crop.png", "https://media.weavy.ai/image/upload/v1792423552/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/kphmokcezmympeksd7aa.png"),
  @("N29 Spatial - Weave\round 7", "n29r7-01_row-of-three-portrait-lightboxes-dark-hall.png", "https://media.weavy.ai/image/upload/v1792423538/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/anp5jvemk13clu0kqefq.png"),
  @("N29 Spatial - Weave\round 7", "n29r7-02_single-screen-hung-on-cables-eye-height.png", "https://media.weavy.ai/image/upload/v1792423546/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/j0l4nnazfjcg62pz974z.png"),
  @("N29 Spatial - Weave\round 7", "n29r7-03_tall-monolith-screen-floor-reflection.png", "https://media.weavy.ai/image/upload/v1792423554/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/nt2u1mygqquiczh6yk0c.png"),
  @("N29 Spatial - Weave\round 7", "n29r7-04_projection-on-hanging-scrim-silhouettes.png", "https://media.weavy.ai/image/upload/v1792423577/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/licwcldsugihbfvfrpvo.png"),
  @("N29 Spatial - Weave\round 7", "n29r7-05_screen-at-end-of-narrow-dark-corridor.png", "https://media.weavy.ai/image/upload/v1792423568/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/gkpm74bq4adn4ljctbcw.png"),
  @("N30 Low Cloud - Weave\round 6", "n30r6-01_billboard-beside-motorway-overpass-fog-wide.png", "https://media.weavy.ai/image/upload/v1792423579/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/gmwrmyufm9zcixanlmm9.png"),
  @("N30 Low Cloud - Weave\round 6", "n30r6-02_screen-above-shopping-centre-entrance-fog-wide.png", "https://media.weavy.ai/image/upload/v1792423588/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ipmsb5ps4imsr75z23yz.png"),
  @("N30 Low Cloud - Weave\round 6", "n30r6-03_billboard-at-roundabout-headlights-fog-wide.png", "https://media.weavy.ai/image/upload/v1792423602/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/m47e3bolcqr2epvsxqhp.png"),
  @("N30 Low Cloud - Weave\round 6", "n30r6-04_portrait-screen-elevated-train-platform-fog.png", "https://media.weavy.ai/image/upload/v1792423604/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/snbuf2mxtelkb5srfmyt.png"),
  @("N30 Low Cloud - Weave\round 6", "n30r6-05_rooftop-billboard-long-street-into-fog.png", "https://media.weavy.ai/image/upload/v1792423614/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/zqvwbvlj90pwomv0hina.png")
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
