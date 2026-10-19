$ErrorActionPreference = "Continue"
$base = "C:\Users\38349\Desktop\01"
$items = @(
  @("N28 Atelier - Weave\round 13", "n28r13-01_show-poster-pasted-on-stone-wall-shadow-passing.png", "https://media.weavy.ai/image/upload/v1792421664/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/gcnqboyxp6cwxdladyhs.png"),
  @("N28 Atelier - Weave\round 13", "n28r13-02_lookbook-open-in-hands-cafe-table.png", "https://media.weavy.ai/image/upload/v1792421671/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/zdqfkibxahuwps56x1an.png"),
  @("N28 Atelier - Weave\round 13", "n28r13-03_bag-on-car-back-seat-door-open-sun.png", "https://media.weavy.ai/image/upload/v1792421678/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/qjd2e6olvde2uuvvqmnn.png"),
  @("N28 Atelier - Weave\round 13", "n28r13-04_invitation-passed-hand-to-hand-in-sun.png", "https://media.weavy.ai/image/upload/v1792421677/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/k48nzbcbimgddh6ow6ar.png"),
  @("N28 Atelier - Weave\round 13", "n28r13-05_bag-on-cafe-chair-water-glass-caustic.png", "https://media.weavy.ai/image/upload/v1792421702/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/bxitthlhkti8ucyv3fcs.png"),
  @("N29 Spatial - Weave\round 6", "n29r6-01_translucent-screen-box-corner-dark-gallery.png", "https://media.weavy.ai/image/upload/v1792421698/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/psf7uxbb5fk5vhfm9j0s.png"),
  @("N29 Spatial - Weave\round 6", "n29r6-02_huge-lightbox-end-of-dark-lobby.png", "https://media.weavy.ai/image/upload/v1792421708/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ohbgvbigj62mgrivp2hy.png"),
  @("N29 Spatial - Weave\round 6", "n29r6-03_dark-hall-stacked-crates-lit-faces.png", "https://media.weavy.ai/image/upload/v1792421711/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/zyrmr3fbp6nbod5rejw1.png"),
  @("N29 Spatial - Weave\round 6", "n29r6-04_wall-of-stacked-crts-sofa-foreground.png", "https://media.weavy.ai/image/upload/v1792421720/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/f0yxbjnjug6buzvbflvh.png"),
  @("N29 Spatial - Weave\round 6", "n29r6-05_huge-projection-end-wall-tiny-silhouettes.png", "https://media.weavy.ai/image/upload/v1792421728/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/bjdotlx5aezjj1uqvtrl.png"),
  @("N30 Low Cloud - Weave\round 5", "n30r5-01_billboard-above-petrol-station-canopy-wide.png", "https://media.weavy.ai/image/upload/v1792421740/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/itf5ivb0yzezmvmb2lpd.png"),
  @("N30 Low Cloud - Weave\round 5", "n30r5-02_billboard-side-of-multistorey-car-park-wide.png", "https://media.weavy.ai/image/upload/v1792421746/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/e5cy6pqxt8zp9olmczxl.png"),
  @("N30 Low Cloud - Weave\round 5", "n30r5-03_billboard-behind-chain-link-fence-empty-lot-wide.png", "https://media.weavy.ai/image/upload/v1792421759/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/oq1nqv2d9x1kmqahrh7f.png"),
  @("N30 Low Cloud - Weave\round 5", "n30r5-04_screen-top-of-metro-entrance-stair.png", "https://media.weavy.ai/image/upload/v1792421764/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/s9nxgetanmqzgamosxcx.png"),
  @("N30 Low Cloud - Weave\round 5", "n30r5-05_rooftop-billboard-past-tram-stop.png", "https://media.weavy.ai/image/upload/v1792421782/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/skf2dr8yvopmzaullyt5.png")
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
