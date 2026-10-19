$ErrorActionPreference = "Continue"
$base = "C:\Users\38349\Desktop\01"
$items = @(
  @("N28 Atelier - Weave\round 9", "n28r9-01_bag-carried-side-crop-hard-sun-stone-wall.png", "https://media.weavy.ai/image/upload/v1792416276/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/gluleiqnghlholkvbrsw.png"),
  @("N28 Atelier - Weave\round 9", "n28r9-02_hang-tag-on-coat-cuff-tight-hard-sun.png", "https://media.weavy.ai/image/upload/v1792416290/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/g22sl7xkmjybv67xxbo9.png"),
  @("N28 Atelier - Weave\round 9", "n28r9-03_hang-tag-at-shirt-collar-very-tight.png", "https://media.weavy.ai/image/upload/v1792416294/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/eod68jxxnpucpsw7sz1n.png"),
  @("N28 Atelier - Weave\round 9", "n28r9-04_invitation-at-hip-mid-stride-hard-shadow.png", "https://media.weavy.ai/image/upload/v1792416302/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/y6yudzfe5u9jh1m75fr6.png"),
  @("N28 Atelier - Weave\round 9", "n28r9-05_bag-past-fluted-shop-window-hard-sun.png", "https://media.weavy.ai/image/upload/v1792416311/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/qrkz1n4ymmxepcwmefev.png"),
  @("N29 Spatial - Weave\round 2", "n29r2-01_backlit-wall-panel-dark-museum-lobby.png", "https://media.weavy.ai/image/upload/v1792416314/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/tnwjrafrgthwjnfo9yyc.png"),
  @("N29 Spatial - Weave\round 2", "n29r2-02_hall-of-suspended-screens.png", "https://media.weavy.ai/image/upload/v1792416321/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ghkomrek9anydurjwu5f.png"),
  @("N29 Spatial - Weave\round 2", "n29r2-03_dark-hall-of-lit-cubes.png", "https://media.weavy.ai/image/upload/v1792416334/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/mconycpigeetwz4z5nlb.png"),
  @("N29 Spatial - Weave\round 2", "n29r2-04_room-of-translucent-screens-dark-hall.png", "https://media.weavy.ai/image/upload/v1792416338/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/l7vqxpi6gemckc3ybvua.png"),
  @("N29 Spatial - Weave\round 2", "n29r2-05_ring-of-screens-on-truss-benches.png", "https://media.weavy.ai/image/upload/v1792416346/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/n5ok5d9e6sk8m0auzeax.png"),
  @("N30 Low Cloud - Weave\round 2", "n30r2-01_led-tower-fog-plaza-dusk.png", "https://media.weavy.ai/image/upload/v1792416369/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/oxqnrzt5jt8o4ihotu4g.png"),
  @("N30 Low Cloud - Weave\round 2", "n30r2-02_wide-screen-plinth-smog-square-dusk.png", "https://media.weavy.ai/image/upload/v1792416370/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/smv3clscgat75exqqzdo.png"),
  @("N30 Low Cloud - Weave\round 2", "n30r2-03_led-facade-screen-corner-building-cloud.png", "https://media.weavy.ai/image/upload/v1792416387/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/cjgxr3up7cdlclnspnjn.png"),
  @("N30 Low Cloud - Weave\round 2", "n30r2-04_roadside-billboard-single-pole-low-cloud.png", "https://media.weavy.ai/image/upload/v1792416410/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/bn7409xdg3njfcyqobqc.png"),
  @("N30 Low Cloud - Weave\round 2", "n30r2-05_rooftop-billboard-over-shuttered-shops-mist.png", "https://media.weavy.ai/image/upload/v1792416401/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/iowmtyrsxhdq1kdql7ip.png")
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
