$ErrorActionPreference = "Continue"
$base = "C:\Users\38349\Desktop\01"
$items = @(
  @("N28 Atelier - Weave\round 20", "n28r20-01_leap-off-step-coat-flaring-bag-frozen.png", "https://media.weavy.ai/image/upload/v1792430443/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/bob7pefvncerlgahf1ew.png"),
  @("N28 Atelier - Weave\round 20", "n28r20-02_lying-on-warm-stone-invitation-on-chest-top-down.png", "https://media.weavy.ai/image/upload/v1792430472/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/x56fo8bhmkd1hrw3gcjh.png"),
  @("N28 Atelier - Weave\round 20", "n28r20-03_bag-tossed-over-shoulder-mid-turn-from-behind.png", "https://media.weavy.ai/image/upload/v1792430470/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/g76zxze29l01uovpfeci.png"),
  @("N28 Atelier - Weave\round 20", "n28r20-04_blade-of-sun-in-dark-passage-hang-tag.png", "https://media.weavy.ai/image/upload/v1792430482/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/mitldcfwydrg9o66zoa9.png"),
  @("N28 Atelier - Weave\round 20", "n28r20-05_seated-fountain-rim-legs-crossed-garment-cover.png", "https://media.weavy.ai/image/upload/v1792430490/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/v7srkdwiywua2srgdiuv.png"),
  @("N28 Atelier - Weave\round 20", "n28r20-06_tiptoe-on-step-edge-bag-behind-calves.png", "https://media.weavy.ai/image/upload/v1792430504/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/kfsvioywu7rzhzhmoi42.png"),
  @("N31 Open Air - Weave\round 4", "n31r4-01_billboard-above-shops-striped-awnings-wide.png", "https://media.weavy.ai/image/upload/v1792430496/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ijp9h3n8uimbyzj8jwxs.png"),
  @("N31 Open Air - Weave\round 4", "n31r4-02_wallscape-terracotta-mediterranean-street-wide.png", "https://media.weavy.ai/image/upload/v1792430507/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/smjmqn2vld8yxmd6o0bv.png"),
  @("N31 Open Air - Weave\round 4", "n31r4-03_banner-on-white-wall-outdoor-pool-wide.png", "https://media.weavy.ai/image/upload/v1792430512/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/dhswdsvihkwjwunpc5py.png"),
  @("N31 Open Air - Weave\round 4", "n31r4-04_billboard-beside-motorway-long-lens-wide.png", "https://media.weavy.ai/image/upload/v1792430520/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/zkb6syf5ayez4pgz3zbp.png"),
  @("N31 Open Air - Weave\round 4", "n31r4-05_side-panel-of-city-bus-at-stop-wide.png", "https://media.weavy.ai/image/upload/v1792430534/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/vfvogpyuliwifa9tnpg6.png"),
  @("N31 Open Air - Weave\round 4", "n31r4-06_lightbox-at-metro-entrance-steps-down.png", "https://media.weavy.ai/image/upload/v1792430539/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/fs8ccslfudtqj1hobqhd.png"),
  @("N31 Open Air - Weave\round 4", "n31r4-07_billboard-on-narrow-corner-building.png", "https://media.weavy.ai/image/upload/v1792430546/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/tu5nhueahjwfhpdbww6d.png"),
  @("N31 Open Air - Weave\round 4", "n31r4-08_banner-under-stone-portico-between-columns.png", "https://media.weavy.ai/image/upload/v1792430551/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/qcoftqmjicg1xhutdoem.png"),
  @("N31 Open Air - Weave\round 4", "n31r4-09_poster-on-plywood-hoarding-tree-shadow.png", "https://media.weavy.ai/image/upload/v1792430561/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/h7qxzwv5f92rhidlh8ih.png"),
  @("N31 Open Air - Weave\round 4", "n31r4-10_poster-beside-doorway-pale-pink-wall.png", "https://media.weavy.ai/image/upload/v1792430566/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/mr7cbf0sn1nnzwo6ej88.png")
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
