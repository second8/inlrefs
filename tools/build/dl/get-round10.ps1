$ErrorActionPreference = "Continue"
$base = "C:\Users\38349\Desktop\01"
$items = @(
  @("N28 Atelier - Weave\round 10", "n28r10-01_garment-cover-carried-by-hanger-walking.png", "https://media.weavy.ai/image/upload/v1792418332/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/lkqrrwzm4r5rtyxgkaty.png"),
  @("N28 Atelier - Weave\round 10", "n28r10-02_seated-stone-steps-bag-beside-boots.png", "https://media.weavy.ai/image/upload/v1792418355/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/rwedncq5chwme5b4hyhz.png"),
  @("N28 Atelier - Weave\round 10", "n28r10-03_hang-tag-on-cardigan-cuff-medium-close.png", "https://media.weavy.ai/image/upload/v1792418372/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/vkhu4ol73s1zzdo6ikdv.png"),
  @("N28 Atelier - Weave\round 10", "n28r10-04_invitation-on-stone-ledge-in-tissue-top-down.png", "https://media.weavy.ai/image/upload/v1792418369/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/d4kbrtfb0ilwo1ntdunz.png"),
  @("N28 Atelier - Weave\round 10", "n28r10-05_bag-held-in-deep-stone-doorway-light.png", "https://media.weavy.ai/image/upload/v1792418383/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/lw4f6uodliaxk6yhow0u.png"),
  @("N29 Spatial - Weave\round 3", "n29r3-01_panel-end-of-long-corridor.png", "https://media.weavy.ai/image/upload/v1792418380/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/dzwsntvshaarch4glh8s.png"),
  @("N29 Spatial - Weave\round 3", "n29r3-02_panel-beside-wide-stone-staircase.png", "https://media.weavy.ai/image/upload/v1792418386/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/icxb2stceihyeizp4snh.png"),
  @("N29 Spatial - Weave\round 3", "n29r3-03_two-storey-atrium-panel-mezzanine-rail.png", "https://media.weavy.ai/image/upload/v1792418395/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/msx8e6f37nqxsrdnsaai.png"),
  @("N29 Spatial - Weave\round 3", "n29r3-04_panel-low-gallery-oak-bench-seated-visitor.png", "https://media.weavy.ai/image/upload/v1792418400/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/tvugn14tzirvy1gb90m7.png"),
  @("N29 Spatial - Weave\round 3", "n29r3-05_panel-through-glass-entrance-wet-plaza.png", "https://media.weavy.ai/image/upload/v1792418413/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ex7d4yoqp0jvy1zoifjn.png")
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
