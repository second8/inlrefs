$ErrorActionPreference = "Continue"
$base = "C:\Users\38349\Desktop\01"
$items = @(
  @("N31 Open Air - Weave\round 6", "n31r6-01_billboard-mirrored-in-rooftop-puddle-wide.png", "https://media.weavy.ai/image/upload/v1792432008/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ztmjwbhavw0q5aanbegi.png"),
  @("N31 Open Air - Weave\round 6", "n31r6-02_billboard-through-open-tram-window-wide.png", "https://media.weavy.ai/image/upload/v1792432016/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/zkmaaznhijmgqvetau6a.png"),
  @("N31 Open Air - Weave\round 6", "n31r6-03_huge-wallscape-tiny-cyclist-below-wide.png", "https://media.weavy.ai/image/upload/v1792432027/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/cbzbge1fzaoepkyljrll.png"),
  @("N31 Open Air - Weave\round 6", "n31r6-04_billboard-across-rooftop-pool-loungers-wide.png", "https://media.weavy.ai/image/upload/v1792432031/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/hsnulfoblpin0tilwell.png"),
  @("N31 Open Air - Weave\round 6", "n31r6-05_three-billboards-in-row-on-one-roof-wide.png", "https://media.weavy.ai/image/upload/v1792432036/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/xcecajjype9hiryggk19.png"),
  @("N31 Open Air - Weave\round 6", "n31r6-06_billboard-above-tennis-court-wide.png", "https://media.weavy.ai/image/upload/v1792432047/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/u7uph5w9pwzhivv8nyxr.png"),
  @("N31 Open Air - Weave\round 6", "n31r6-07_billboard-from-car-passenger-seat-wide.png", "https://media.weavy.ai/image/upload/v1792432052/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/wuse9rnhbcbdil52sgul.png"),
  @("N31 Open Air - Weave\round 6", "n31r6-08_wallscape-with-giant-diagonal-building-shadow-wide.png", "https://media.weavy.ai/image/upload/v1792432061/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/csumjjbmcopwxqpuziv1.png"),
  @("N31 Open Air - Weave\round 6", "n31r6-09_zebra-crossing-leading-to-billboard-wide.png", "https://media.weavy.ai/image/upload/v1792432068/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/taggegvuzlquschpk7sm.png"),
  @("N31 Open Air - Weave\round 6", "n31r6-10_billboard-through-railway-viaduct-arch-wide.png", "https://media.weavy.ai/image/upload/v1792432075/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/pyylpx9pdem8toz4tdes.png"),
  @("N31 Open Air - Weave\round 6", "n31r6-11_billboard-beside-golden-wheat-field-wide.png", "https://media.weavy.ai/image/upload/v1792432084/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/vskdkzgaa3bdgnf6fg76.png"),
  @("N31 Open Air - Weave\round 6", "n31r6-12_flock-of-birds-over-billboard-wide.png", "https://media.weavy.ai/image/upload/v1792432090/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/fxpyx03zqzsbhbvwtkwt.png"),
  @("N31 Open Air - Weave\round 6", "n31r6-13_skatepark-poster-wall-over-concrete-bowl-wide.png", "https://media.weavy.ai/image/upload/v1792432097/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/zuecrvldpuxpxb6sygz0.png"),
  @("N31 Open Air - Weave\round 6", "n31r6-14_banner-across-amphitheatre-concrete-steps-wide.png", "https://media.weavy.ai/image/upload/v1792432109/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/qnz2yh1ze6l5af3ajoxm.png"),
  @("N31 Open Air - Weave\round 6", "n31r6-15_long-banner-on-pier-railing-over-turquoise-sea-wide.png", "https://media.weavy.ai/image/upload/v1792432111/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/zmau6xyajenkhabgor8u.png"),
  @("N31 Open Air - Weave\round 6", "n31r6-16_wallscape-with-window-cleaner-cradle.png", "https://media.weavy.ai/image/upload/v1792432126/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/fwtd7shpem4y9n8nfhfo.png"),
  @("N31 Open Air - Weave\round 6", "n31r6-17_poster-seen-through-ferry-porthole.png", "https://media.weavy.ai/image/upload/v1792432135/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/qcgi128ykxuifn4yul9q.png"),
  @("N31 Open Air - Weave\round 6", "n31r6-18_billboard-through-gap-in-clipped-hedge.png", "https://media.weavy.ai/image/upload/v1792432139/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/yscqx9dmuvxh42x9po04.png"),
  @("N31 Open Air - Weave\round 6", "n31r6-19_walker-blurred-past-sunlit-lightbox.png", "https://media.weavy.ai/image/upload/v1792432148/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/zvhrxvbxrekz494h4rkv.png"),
  @("N31 Open Air - Weave\round 6", "n31r6-20_billboard-at-top-of-long-hill-stair.png", "https://media.weavy.ai/image/upload/v1792432154/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/l3vyc6hlqfziy1nlrdz2.png"),
  @("N31 Open Air - Weave\round 6", "n31r6-21_poster-with-bicycle-leaning-below.png", "https://media.weavy.ai/image/upload/v1792432163/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/t0xpzpc3qwjw2wva2ggb.png"),
  @("N31 Open Air - Weave\round 6", "n31r6-22_banner-strung-between-two-balconies-over-lane.png", "https://media.weavy.ai/image/upload/v1792432170/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/hqpynqs6u23papeethfa.png"),
  @("N31 Open Air - Weave\round 6", "n31r6-23_poster-on-white-lighthouse.png", "https://media.weavy.ai/image/upload/v1792432178/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ay2cgycmjd4jqlfbcntu.png"),
  @("N31 Open Air - Weave\round 6", "n31r6-24_billboard-on-cliffside-road-sea-behind.png", "https://media.weavy.ai/image/upload/v1792432187/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/rglcblbke1uevmnuwbhg.png"),
  @("N31 Open Air - Weave\round 6", "n31r6-25_poster-above-fruit-stall-awning.png", "https://media.weavy.ai/image/upload/v1792432197/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/xinuf602sxujxvi54bak.png"),
  @("N31 Open Air - Weave\round 6", "n31r6-26_worker-on-ladder-smoothing-fresh-poster.png", "https://media.weavy.ai/image/upload/v1792432205/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/xmzzm5gsbr6hmc9xz1ro.png"),
  @("N31 Open Air - Weave\round 6", "n31r6-27_crew-on-billboard-catwalk.png", "https://media.weavy.ai/image/upload/v1792432214/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/jtefdelayrn4uodzthoj.png"),
  @("N31 Open Air - Weave\round 6", "n31r6-28_poster-at-top-of-escalator-into-sunlight.png", "https://media.weavy.ai/image/upload/v1792432220/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/kcr0d3vz2pm0fp7h2xxq.png"),
  @("N31 Open Air - Weave\round 6", "n31r6-29_billboard-seen-from-inside-dark-garage.png", "https://media.weavy.ai/image/upload/v1792432225/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/wlkibrxjqqjaxzbckwmz.png"),
  @("N31 Open Air - Weave\round 6", "n31r6-30_poster-above-stone-drinking-fountain.png", "https://media.weavy.ai/image/upload/v1792432233/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/kympbqsrbeggkr7ueh4r.png")
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
