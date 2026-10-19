$ErrorActionPreference = "Continue"
$base = "C:\Users\38349\Desktop\01"
$items = @(
  @("N28 Atelier - Weave\round 11", "n28r11-01_bag-hooked-over-forearm-stone-balustrade.png", "https://media.weavy.ai/image/upload/v1792419076/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ossu9nbzicq4zjcdvovp.png"),
  @("N28 Atelier - Weave\round 11", "n28r11-02_garment-cover-on-hook-sunlit-stone-doorway.png", "https://media.weavy.ai/image/upload/v1792419069/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ardbpmy89umw2k8kqpcj.png"),
  @("N28 Atelier - Weave\round 11", "n28r11-03_invitation-between-fingers-at-side-mid-stride.png", "https://media.weavy.ai/image/upload/v1792419086/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/iixufdvqxodcriyxzgw2.png"),
  @("N28 Atelier - Weave\round 11", "n28r11-04_bag-on-stone-ledge-hang-tag-on-handle.png", "https://media.weavy.ai/image/upload/v1792419100/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/nbex7geahc85lcemcsj4.png"),
  @("N28 Atelier - Weave\round 11", "n28r11-05_garment-cover-past-fluted-shop-glass.png", "https://media.weavy.ai/image/upload/v1792419105/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/jl2ebtjkrmfnsfhrxaw6.png"),
  @("N29 Spatial - Weave\round 4", "n29r4-01_backlit-wall-hall-new-angle.png", "https://media.weavy.ai/image/upload/v1792419113/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/vqm6ipz1vjh7oi821r61.png"),
  @("N29 Spatial - Weave\round 4", "n29r4-02_stack-of-grey-crts-one-white-image.png", "https://media.weavy.ai/image/upload/v1792419113/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/y9b90iwd2lug93cgmhub.png"),
  @("N29 Spatial - Weave\round 4", "n29r4-03_lit-wooden-cubes-grouped-on-floor.png", "https://media.weavy.ai/image/upload/v1792419121/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/xpgplpkjgfucmpxjcgjw.png"),
  @("N29 Spatial - Weave\round 4", "n29r4-04_translucent-screen-room-box.png", "https://media.weavy.ai/image/upload/v1792419132/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/eixzx2fortccegrbdxct.png"),
  @("N29 Spatial - Weave\round 4", "n29r4-05_large-screen-hanging-on-wires.png", "https://media.weavy.ai/image/upload/v1792419140/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/tkck271rwxlpvtr241pw.png"),
  @("N30 Low Cloud - Weave\round 3", "n30r3-01_long-led-screen-river-embankment-wide.png", "https://media.weavy.ai/image/upload/v1792419144/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/kowwsfp1sfawr95jcq7j.png"),
  @("N30 Low Cloud - Weave\round 3", "n30r3-02_rooftop-billboard-across-boulevard-wide.png", "https://media.weavy.ai/image/upload/v1792419157/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/lytol6ud4zakoidzhpjy.png"),
  @("N30 Low Cloud - Weave\round 3", "n30r3-03_arena-led-screen-empty-plaza-wide.png", "https://media.weavy.ai/image/upload/v1792419168/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/tcyrqveakeylz5ajzdb2.png"),
  @("N30 Low Cloud - Weave\round 3", "n30r3-04_tall-banner-screen-facade-side-street.png", "https://media.weavy.ai/image/upload/v1792419174/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/fqwp0innzpwho4oattqw.png"),
  @("N30 Low Cloud - Weave\round 3", "n30r3-05_two-pole-billboard-bridge-end-wet-road.png", "https://media.weavy.ai/image/upload/v1792419190/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/qehiyxbkokx39pxny2gv.png")
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
