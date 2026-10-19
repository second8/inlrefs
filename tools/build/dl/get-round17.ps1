$ErrorActionPreference = "Continue"
$base = "C:\Users\38349\Desktop\01"
$items = @(
  @("N31 Open Air - Weave\round 1", "n31r1-01_wallscape-on-white-industrial-building-wide.png", "https://media.weavy.ai/image/upload/v1792427050/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/menbwdowebjqvq6sz0bz.png"),
  @("N31 Open Air - Weave\round 1", "n31r1-02_backlit-station-poster-train-blur.png", "https://media.weavy.ai/image/upload/v1792427056/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/srrydfvgn3gkm2yfctd0.png"),
  @("N31 Open Air - Weave\round 1", "n31r1-03_run-of-posters-on-hoarding-under-overpass-wide.png", "https://media.weavy.ai/image/upload/v1792427108/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/vbjbnuuhr9jk7ilcnbdk.png"),
  @("N31 Open Air - Weave\round 1", "n31r1-04_pole-billboard-against-empty-blue-sky.png", "https://media.weavy.ai/image/upload/v1792427117/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/iqfdzrohtoe10arylljh.png"),
  @("N31 Open Air - Weave\round 1", "n31r1-05_rooftop-billboard-on-old-brick-building-wide.png", "https://media.weavy.ai/image/upload/v1792427125/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/p1tfqrezmrdrn2fyvulo.png"),
  @("N31 Open Air - Weave\round 1", "n31r1-06_long-poster-on-white-subway-tiles-wide.png", "https://media.weavy.ai/image/upload/v1792427128/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/scz0qlfloiminimhg7f9.png"),
  @("N31 Open Air - Weave\round 1", "n31r1-07_billboard-in-white-concrete-courtyard.png", "https://media.weavy.ai/image/upload/v1792427137/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/sbo18r4cn8dqypbu2bvt.png"),
  @("N31 Open Air - Weave\round 1", "n31r1-08_banner-on-mesh-wrapped-scaffold.png", "https://media.weavy.ai/image/upload/v1792427145/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/buoxfh5tvzlgahgndckr.png"),
  @("N28 Atelier - Weave\round 17", "n28r17-01_appointment-card-tucked-into-glove-cuff.png", "https://media.weavy.ai/image/upload/v1792427312/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/nl7sy5zfcghapcorewou.png"),
  @("N28 Atelier - Weave\round 17", "n28r17-02_wax-sealed-envelope-gloved-fingertips-on-stone.png", "https://media.weavy.ai/image/upload/v1792427322/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ai3vyazxfd31jffdsygd.png"),
  @("N28 Atelier - Weave\round 17", "n28r17-03_garment-cover-seen-from-dark-atelier-doorway.png", "https://media.weavy.ai/image/upload/v1792427338/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ttsvn3fvbwrm1cyz6gzp.png"),
  @("N28 Atelier - Weave\round 17", "n28r17-04_bag-mid-swing-pavement-level-long-shadow.png", "https://media.weavy.ai/image/upload/v1792427347/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ipk6b8mvdghlbrfh6ftr.png"),
  @("N28 Atelier - Weave\round 17", "n28r17-05_unboxing-coat-in-tissue-note-card-top-down.png", "https://media.weavy.ai/image/upload/v1792427354/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/sc8efijj1slaqqov6liv.png")
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
