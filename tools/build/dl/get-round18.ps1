$ErrorActionPreference = "Continue"
$base = "C:\Users\38349\Desktop\01"
$items = @(
  @("N28 Atelier - Weave\round 18", "n28r18-01_birds-eye-garment-cover-laid-flat-long-shadow.png", "https://media.weavy.ai/image/upload/v1792427964/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/zxecwj9zkxlz9bkykmn6.png"),
  @("N28 Atelier - Weave\round 18", "n28r18-02_invitation-held-out-with-its-shadow-double-on-wall.png", "https://media.weavy.ai/image/upload/v1792427976/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/mu7jbfflvihk9sujbums.png"),
  @("N28 Atelier - Weave\round 18", "n28r18-03_tower-of-ribbon-tied-boxes-in-gloved-arms.png", "https://media.weavy.ai/image/upload/v1792427985/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/jfbjm1aibvlvkivcv0bq.png"),
  @("N28 Atelier - Weave\round 18", "n28r18-04_hang-tag-spinning-from-gloved-finger-shadow-on-stone.png", "https://media.weavy.ai/image/upload/v1792428002/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/yrt9fwgmhb9rljqojuvn.png"),
  @("N28 Atelier - Weave\round 18", "n28r18-05_editorial-crouch-on-steps-bag-at-boots.png", "https://media.weavy.ai/image/upload/v1792428010/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ravjvy6cxp3w9aefwg4j.png"),
  @("N31 Open Air - Weave\round 2", "n31r2-01_three-small-posters-on-black-hoarding-bench-wide.png", "https://media.weavy.ai/image/upload/v1792428009/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/eepq4nbv1u8sgjdmb3fg.png"),
  @("N31 Open Air - Weave\round 2", "n31r2-02_poster-on-pale-corrugated-metal-wall-wide.png", "https://media.weavy.ai/image/upload/v1792428018/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/dxiblz97phd2ienjav7x.png"),
  @("N31 Open Air - Weave\round 2", "n31r2-03_ad-on-side-of-parked-truck-trailer-wide.png", "https://media.weavy.ai/image/upload/v1792428029/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/vqmtsx51hydhegs9jnuk.png"),
  @("N31 Open Air - Weave\round 2", "n31r2-04_long-billboard-under-bridge-shade-bright-street-wide.png", "https://media.weavy.ai/image/upload/v1792428030/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/qorwz8eiroep7sc1phg5.png"),
  @("N31 Open Air - Weave\round 2", "n31r2-05_clean-long-poster-on-white-subway-tiles-wide.png", "https://media.weavy.ai/image/upload/v1792428038/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/xrawfzef2qplef4kf0io.png"),
  @("N31 Open Air - Weave\round 2", "n31r2-06_bus-shelter-panel-sunny-kerb.png", "https://media.weavy.ai/image/upload/v1792428048/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/dznnuztxvluqvihkqdvd.png"),
  @("N31 Open Air - Weave\round 2", "n31r2-07_banner-wrapping-side-of-tall-building.png", "https://media.weavy.ai/image/upload/v1792428054/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/abciykozlsfawmmrhuxe.png"),
  @("N31 Open Air - Weave\round 2", "n31r2-08_billboard-above-tree-lined-avenue.png", "https://media.weavy.ai/image/upload/v1792428061/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/o8sdfapqtpi3ruqi7n5w.png"),
  @("N31 Open Air - Weave\round 2", "n31r2-09_digital-totem-in-sunny-plaza.png", "https://media.weavy.ai/image/upload/v1792428069/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/unxefg12k2bcd2zrlo8x.png"),
  @("N31 Open Air - Weave\round 2", "n31r2-10_billboard-on-white-rooftop-from-terrace.png", "https://media.weavy.ai/image/upload/v1792428077/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/y91ofsgf6bcfs9wyduxh.png")
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
