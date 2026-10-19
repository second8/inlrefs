$ErrorActionPreference = "Continue"
$base = "C:\Users\38349\Desktop\01"
$items = @(
  @("N28 Atelier - Weave\round 16", "n28r16-01_bag-from-fingertips-against-stone-column.png", "https://media.weavy.ai/image/upload/v1792425767/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/uzz9o1hqfkfwhkuj5kzy.png"),
  @("N28 Atelier - Weave\round 16", "n28r16-02_invitation-in-gloved-hand-against-coat-lapel.png", "https://media.weavy.ai/image/upload/v1792425783/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/qacpobyw8ifrdmmqzt8g.png"),
  @("N28 Atelier - Weave\round 16", "n28r16-03_clothing-box-on-knee-seated-stone-steps.png", "https://media.weavy.ai/image/upload/v1792425832/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/rlmqva0qb8zzjmpa6rhx.png"),
  @("N28 Atelier - Weave\round 16", "n28r16-04_garment-cover-over-shoulder-walking-away-colonnade.png", "https://media.weavy.ai/image/upload/v1792425808/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ivcbyowh8urch7gewagg.png"),
  @("N28 Atelier - Weave\round 16", "n28r16-05_gloved-hand-turns-coat-cuff-hang-tag.png", "https://media.weavy.ai/image/upload/v1792425808/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ax2zovvc0musvl6brwvt.png"),
  @("N30 Low Cloud - Weave\round 7", "n30r7-01_billboard-behind-bus-depot-fog-wide.png", "https://media.weavy.ai/image/upload/v1792425816/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/oaylf90tn6fhowzutnjc.png"),
  @("N30 Low Cloud - Weave\round 7", "n30r7-02_billboard-on-slope-above-suburban-road-fog-wide.png", "https://media.weavy.ai/image/upload/v1792425825/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/gca4j51uzb3hykb9s8ru.png"),
  @("N30 Low Cloud - Weave\round 7", "n30r7-03_billboard-on-harbour-edge-cranes-in-fog-wide.png", "https://media.weavy.ai/image/upload/v1792425838/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/gmhflzeyikzj0iiukqxv.png"),
  @("N30 Low Cloud - Weave\round 7", "n30r7-04_billboard-beside-level-crossing-fog-wide.png", "https://media.weavy.ai/image/upload/v1792425842/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/gwcwcemk9rureofyhurs.png"),
  @("N30 Low Cloud - Weave\round 7", "n30r7-05_billboard-on-warehouse-roof-ring-road-fog-wide.png", "https://media.weavy.ai/image/upload/v1792425853/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/rhqg5w5vmrob3dj0rfhb.png"),
  @("N30 Low Cloud - Weave\round 7", "n30r7-06_portrait-screen-at-pedestrian-underpass-entrance-fog.png", "https://media.weavy.ai/image/upload/v1792425859/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/omcu59jwzobunbpkg585.png"),
  @("N30 Low Cloud - Weave\round 7", "n30r7-07_poster-billboard-end-of-narrow-residential-street-fog.png", "https://media.weavy.ai/image/upload/v1792425870/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/h1psf89zhvy6jegfty1l.png"),
  @("N30 Low Cloud - Weave\round 7", "n30r7-08_portrait-screen-at-parking-garage-ramp-fog.png", "https://media.weavy.ai/image/upload/v1792425877/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ndtnprdh9vaymflrelqh.png"),
  @("N30 Low Cloud - Weave\round 7", "n30r7-09_billboard-above-canal-from-footbridge-fog.png", "https://media.weavy.ai/image/upload/v1792425887/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ejt4wytcxrt1r4oxcoge.png"),
  @("N30 Low Cloud - Weave\round 7", "n30r7-10_pole-screen-small-square-bare-trees-fog.png", "https://media.weavy.ai/image/upload/v1792425900/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/p9o61qkngmscz5yuf9vt.png")
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
