$ErrorActionPreference = "Continue"
$base = "C:\Users\38349\Desktop\01"
$items = @(
  @("N28 Atelier - Weave\round 12", "n28r12-01_invitation-in-gap-between-fluted-glass-doors.png", "https://media.weavy.ai/image/upload/v1792420267/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ldddzxhalkdxkduchdfh.png"),
  @("N28 Atelier - Weave\round 12", "n28r12-02_bag-on-glass-shelf-shop-window.png", "https://media.weavy.ai/image/upload/v1792420268/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/cbcyqerez3wsror43z6n.png"),
  @("N28 Atelier - Weave\round 12", "n28r12-03_hang-tag-on-cuff-by-glass-block-caustics.png", "https://media.weavy.ai/image/upload/v1792420307/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/bjx6rxjyrz0addhimh8j.png"),
  @("N28 Atelier - Weave\round 12", "n28r12-04_garment-cover-before-glass-brick-wall.png", "https://media.weavy.ai/image/upload/v1792420288/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/yvyiwvv3arqz7bsvwjl5.png"),
  @("N28 Atelier - Weave\round 12", "n28r12-05_invitation-on-ledge-glass-caustic-top-down.png", "https://media.weavy.ai/image/upload/v1792420311/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/jzp6ryto7hm1lc5dgcbq.png"),
  @("N29 Spatial - Weave\round 5", "n29r5-01_backlit-wall-hall-new-angle.png", "https://media.weavy.ai/image/upload/v1792420309/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/q5sf1jnbq3z5gigvoeqp.png"),
  @("N29 Spatial - Weave\round 5", "n29r5-02_stack-of-grey-crts-one-white-image.png", "https://media.weavy.ai/image/upload/v1792420382/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/zfmtdfzvlymrvclcjyzs.png"),
  @("N29 Spatial - Weave\round 5", "n29r5-03_lit-wooden-cubes-grouped-on-floor.png", "https://media.weavy.ai/image/upload/v1792420333/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/wuvx5newu0qbt9ezk6l9.png"),
  @("N29 Spatial - Weave\round 5", "n29r5-04_translucent-screen-room-box.png", "https://media.weavy.ai/image/upload/v1792420346/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/dl2wrvnid34gontyn2i6.png"),
  @("N29 Spatial - Weave\round 5", "n29r5-05_large-screen-hanging-on-wires.png", "https://media.weavy.ai/image/upload/v1792420427/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/wsqywykawtnn4rhdarlt.png"),
  @("N30 Low Cloud - Weave\round 4", "n30r4-01_standard-billboard-low-rooftop-crossroads-wide.png", "https://media.weavy.ai/image/upload/v1792420416/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/lni74ksjw8ngyreinngk.png"),
  @("N30 Low Cloud - Weave\round 4", "n30r4-02_led-screen-building-corner-shopping-street-wide.png", "https://media.weavy.ai/image/upload/v1792420369/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ukth8dylyv5u9fxlfdzb.png"),
  @("N30 Low Cloud - Weave\round 4", "n30r4-03_billboard-wall-beside-railway-from-platform-wide.png", "https://media.weavy.ai/image/upload/v1792420371/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/xjs9zgdedccnxtyrb3ck.png"),
  @("N30 Low Cloud - Weave\round 4", "n30r4-04_poster-billboard-apartment-side-wall.png", "https://media.weavy.ai/image/upload/v1792420412/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/dds9ek7pcnlgsc9ajexz.png"),
  @("N30 Low Cloud - Weave\round 4", "n30r4-05_portrait-digital-screen-pole-pedestrian-street.png", "https://media.weavy.ai/image/upload/v1792420395/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/g9c3gltk45rhshdocdig.png")
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
