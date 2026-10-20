$ErrorActionPreference = "Continue"
$base = "C:\Users\38349\Desktop\01"
$items = @(
  @("N31 Open Air - Weave\round 8", "n31r8-01_lone-billboard-on-scaffold-steppe-empty-frame-beside.png", "https://media.weavy.ai/image/upload/v1792488694/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/h6bdhqm8njsdky2qbxhb.png"),
  @("N31 Open Air - Weave\round 8", "n31r8-02_billboard-beside-straight-empty-steppe-road.png", "https://media.weavy.ai/image/upload/v1792488701/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/px4dargemwackrtfxl3o.png"),
  @("N31 Open Air - Weave\round 8", "n31r8-03_billboard-across-dry-gravel-riverbed.png", "https://media.weavy.ai/image/upload/v1792488715/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ll6akrmnxo4jhebfw7ol.png"),
  @("N31 Open Air - Weave\round 8", "n31r8-04_billboard-behind-wire-fence-tall-grass.png", "https://media.weavy.ai/image/upload/v1792488717/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/jkredhgf3vd3jelpg88u.png"),
  @("N31 Open Air - Weave\round 8", "n31r8-05_billboard-before-far-snowy-range.png", "https://media.weavy.ai/image/upload/v1792488724/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/es5viarokf5gfpisit0l.png"),
  @("N32 Restaurant - Weave\round 1", "n32r1-01_menu-card-on-marble-ribbed-glass-caustic-top-down.png", "https://media.weavy.ai/image/upload/v1792488741/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/qqslw24mirvdzhr6qpzn.png"),
  @("N32 Restaurant - Weave\round 1", "n32r1-02_stack-of-coasters-bronze-bar-table-amber-coupe.png", "https://media.weavy.ai/image/upload/v1792488751/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/mqgfcvmbrymlgknecevc.png"),
  @("N32 Restaurant - Weave\round 1", "n32r1-03_coaster-on-olive-linen-tipped-coupe-caustic.png", "https://media.weavy.ai/image/upload/v1792488751/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/mgmtbv4tbl6bk1w7ekyl.png"),
  @("N32 Restaurant - Weave\round 1", "n32r1-04_reservation-card-white-tablecloth-wine-glass-light.png", "https://media.weavy.ai/image/upload/v1792488760/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/vcc1mssy9szvbnuskqib.png"),
  @("N32 Restaurant - Weave\round 1", "n32r1-05_business-card-walnut-bar-top-whisky-caustic.png", "https://media.weavy.ai/image/upload/v1792488761/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/vjs1p8bbero1cgkwjmpz.png"),
  @("N33 Devices - Weave\round 1", "n33r1-01_brushed-aluminium-control-unit-two-dials.png", "https://media.weavy.ai/image/upload/v1792488841/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/qwiyw4yz8lagyto89ghx.png"),
  @("N33 Devices - Weave\round 1", "n33r1-02_ev-charging-pillar-portrait-screen.png", "https://media.weavy.ai/image/upload/v1792488781/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/gofwg3my6wq1wnpwlyf2.png"),
  @("N33 Devices - Weave\round 1", "n33r1-03_rounded-handheld-screen-over-three-buttons.png", "https://media.weavy.ai/image/upload/v1792488789/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/zegdhfcxeuyyouhegv16.png"),
  @("N33 Devices - Weave\round 1", "n33r1-04_wall-thermostat-panel-square-screen.png", "https://media.weavy.ai/image/upload/v1792488810/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/oosih76hd1n2sy707ini.png"),
  @("N33 Devices - Weave\round 1", "n33r1-05_smart-home-hub-on-aluminium-stand.png", "https://media.weavy.ai/image/upload/v1792488797/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/mhrzaovbwb6v0c8k3i9c.png"),
  @("N34 Desk Light - Weave\round 1", "n34r1-01_laptop-on-oak-desk-late-sun-water-glass.png", "https://media.weavy.ai/image/upload/v1792488816/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/b8i1gn9ncqbfzhwrzghz.png"),
  @("N34 Desk Light - Weave\round 1", "n34r1-02_ipad-on-oak-desk-ceramic-mug-top-down.png", "https://media.weavy.ai/image/upload/v1792488820/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/i1iyplpux1gahywvax5g.png"),
  @("N34 Desk Light - Weave\round 1", "n34r1-03_phone-and-notebook-oak-desk-top-down.png", "https://media.weavy.ai/image/upload/v1792488835/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/pz0zqjeznmkellemzrww.png"),
  @("N34 Desk Light - Weave\round 1", "n34r1-04_monitor-on-oak-desk-white-wall-plant-shadow.png", "https://media.weavy.ai/image/upload/v1792488835/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/wb0bzs3lwctm2ic4orid.png"),
  @("N34 Desk Light - Weave\round 1", "n34r1-05_poster-behind-studio-window-street-reflections.png", "https://media.weavy.ai/image/upload/v1792488841/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/lm7htvhoepmtq7le44jr.png")
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
