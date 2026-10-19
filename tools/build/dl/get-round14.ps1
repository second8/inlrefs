$ErrorActionPreference = "Continue"
$base = "C:\Users\38349\Desktop\01"
$items = @(
  @("N28 Atelier - Weave\round 14", "n28r14-01_woven-neck-label-inside-coat-collar-from-behind.png", "https://media.weavy.ai/image/upload/v1792422638/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/m0zzsztf2wxvljxbpkbg.png"),
  @("N28 Atelier - Weave\round 14", "n28r14-02_printed-tee-on-oak-hanger-sunlit-doorway.png", "https://media.weavy.ai/image/upload/v1792422636/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/aiq3dnkzoj5dwojmrdfb.png"),
  @("N28 Atelier - Weave\round 14", "n28r14-03_cotton-dust-bag-on-stone-ledge-by-boots.png", "https://media.weavy.ai/image/upload/v1792422650/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/qyhs4zilekxo7dkj1hi2.png"),
  @("N28 Atelier - Weave\round 14", "n28r14-04_tissue-seal-inside-open-bag-top-down.png", "https://media.weavy.ai/image/upload/v1792422656/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/koyh2rouucn4pyilj0pl.png"),
  @("N28 Atelier - Weave\round 14", "n28r14-05_atelier-nameplate-beside-stone-doorway.png", "https://media.weavy.ai/image/upload/v1792422765/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/arygggkeqtb9sls5chhx.png")
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
