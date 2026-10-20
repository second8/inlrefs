$ErrorActionPreference = "Continue"
$base = "C:\Users\38349\Desktop\01"
$items = @(
  @("N32 Restaurant - Weave\round 2", "n32r2-01_menu-card-marble-clear-ribbed-carafe-caustic-fork.png", "https://media.weavy.ai/image/upload/v1792490674/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/l7zyd2up4kgqrdumzj9y.png"),
  @("N32 Restaurant - Weave\round 2", "n32r2-02_tall-wine-list-in-bronze-stand-white-cloth-flute.png", "https://media.weavy.ai/image/upload/v1792490675/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/l61656kwfdkib0xg1gqv.png"),
  @("N32 Restaurant - Weave\round 2", "n32r2-03_place-card-ivory-linen-folded-napkin-tumbler.png", "https://media.weavy.ai/image/upload/v1792490718/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/cj6mvhh6qxhzdzxlc1o5.png"),
  @("N32 Restaurant - Weave\round 2", "n32r2-04_single-coaster-bronze-table-two-crystal-tumblers.png", "https://media.weavy.ai/image/upload/v1792490692/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/daqrzwu0eizebystw5rz.png"),
  @("N32 Restaurant - Weave\round 2", "n32r2-05_bill-card-on-bronze-tray-two-espresso-cups.png", "https://media.weavy.ai/image/upload/v1792490701/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/iuqdrjza5avxp06o5d1w.png"),
  @("N32 Restaurant - Weave\round 2", "n32r2-06_hand-setting-coaster-on-marble-bar-coupe.png", "https://media.weavy.ai/image/upload/v1792490708/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/mszimylxvjrocbeqtrbr.png"),
  @("N32 Restaurant - Weave\round 2", "n32r2-07_white-matchbox-marble-candle-votive-glow.png", "https://media.weavy.ai/image/upload/v1792490710/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/fnqdt6jfqoeajlawtbs9.png"),
  @("N32 Restaurant - Weave\round 2", "n32r2-08_paper-napkin-band-white-cloth-silverware.png", "https://media.weavy.ai/image/upload/v1792490725/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/wernjsurqid1r4rasvmd.png"),
  @("N32 Restaurant - Weave\round 2", "n32r2-09_menu-in-marble-block-on-bronze-bar-counter.png", "https://media.weavy.ai/image/upload/v1792490731/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/umfxx7zza3rlpjwincgo.png"),
  @("N32 Restaurant - Weave\round 2", "n32r2-10_gift-card-in-open-envelope-ivory-linen-coupe.png", "https://media.weavy.ai/image/upload/v1792490737/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/tppg9yqbssmkw22kt00z.png"),
  @("N32 Restaurant - Weave\round 2", "n32r2-11_wine-bottle-blank-label-marble-glass.png", "https://media.weavy.ai/image/upload/v1792490749/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/uelx4jcmfiqzag6c1jrv.png"),
  @("N32 Restaurant - Weave\round 2", "n32r2-12_pastry-box-lid-marble-champagne-flute.png", "https://media.weavy.ai/image/upload/v1792490757/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/wurwnwxdrwxgzurfnmim.png"),
  @("N32 Restaurant - Weave\round 2", "n32r2-13_table-number-card-set-table-for-two-candle.png", "https://media.weavy.ai/image/upload/v1792490760/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/dlv5nfvv5bbzrzxaaehs.png"),
  @("N32 Restaurant - Weave\round 2", "n32r2-15_open-two-panel-menu-white-cloth-glass-shadows.png", "https://media.weavy.ai/image/upload/v1792490794/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/lto4glot6k9kwj0gvbtm.png"),
  @("N32 Restaurant - Weave\round 2", "n32r2-16_business-card-between-fingers-over-marble.png", "https://media.weavy.ai/image/upload/v1792490788/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/kupsssnfqxjn3lz78jzn.png"),
  @("N32 Restaurant - Weave\round 2", "n32r2-17_dessert-card-leaning-on-carafe-ivory-linen.png", "https://media.weavy.ai/image/upload/v1792490801/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/asoysrejr33voxroyy2r.png"),
  @("N32 Restaurant - Weave\round 2", "n32r2-18_receipt-slip-on-bronze-dish-two-mints.png", "https://media.weavy.ai/image/upload/v1792490807/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/m8ttlmtrcqo63srkstzu.png"),
  @("N32 Restaurant - Weave\round 2", "n32r2-19_long-menu-strip-on-folded-napkin-charger-plate.png", "https://media.weavy.ai/image/upload/v1792490812/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/kqyxbzfdhruu1zhg3ajf.png"),
  @("N32 Restaurant - Weave\round 2", "n32r2-20_reservation-card-bronze-table-champagne-bucket-glow.png", "https://media.weavy.ai/image/upload/v1792490820/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/n8ow8qxzcyhu2dd8qhco.png")
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
