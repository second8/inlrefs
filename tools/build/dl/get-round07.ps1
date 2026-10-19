$ErrorActionPreference = "Continue"
$base = "C:\Users\38349\Desktop\01"
$items = @(
  @("N28 Atelier - Weave\round 7", "n28r7-01_invitation-prism-ghost-plaster-wall.png", "https://media.weavy.ai/image/upload/v1792412659/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/hocaty5q1of9doijrjis.png"),
  @("N28 Atelier - Weave\round 7", "n28r7-02_garment-cover-in-open-glass-vitrine.png", "https://media.weavy.ai/image/upload/v1792412655/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/j8gsd9ygd2v3ioehr0r9.png"),
  @("N28 Atelier - Weave\round 7", "n28r7-03_bag-carried-past-glass-door-satin-sliced.png", "https://media.weavy.ai/image/upload/v1792412678/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/rextvgnsw0n8yoil8et5.png"),
  @("N28 Atelier - Weave\round 7", "n28r7-04_hang-tag-on-cuff-on-vitrine-glass-top-down.png", "https://media.weavy.ai/image/upload/v1792412690/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ntwv0jy6jfbkzm1fhs53.png"),
  @("N28 Atelier - Weave\round 7", "n28r7-05_bag-handed-out-of-fitting-room.png", "https://media.weavy.ai/image/upload/v1792412703/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/lsnaknirtrsmb6eprdag.png")
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
