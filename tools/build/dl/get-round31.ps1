$ErrorActionPreference = "Continue"
$base = "C:\Users\38349\Desktop\01"
$items = @(
  @("N35 Nature - Weave\round 1", "n35r1-02_ipad-upright-on-mossy-stone-fern-forest-lite.jpg", "https://s3-alpha-sig.figma.com/img/d781/68e2/e230038ac142653b4ef6621f93dc817b.jpg?Expires=1796601600&Key-Pair-Id=APKAQ4GOSFWCW27IBOMQ&Signature=H6KbeCqrTAK29V2gkLU3y40Nxl-I6VkHvAk0F2VNcask-53Tuzg1oVW43XKBRL8DCJXOirYiz165K2c8T8jwTQB5IcsfM89gn8BTxdqEsNYHWZdkEsFHVM0YgDfW0OegC5OdRZOXgGTALS0fInJGTxa9yGzo2lOkaK3jSMFT51tFeIy0WGdy7rtnFcKZfSNSI6kQOvA2ZTTf31qz3t63RaJi-BympSy8svu2R2V8jWYyq3fZl6wQa-sWVOv8WRrE0omz-TyWK2hoM4Qu-K1JHDaGQzo8Vc8xGI1kQjR7I6C9luCGrBvLD1Vqbhz4733cHqXY15Uamxc-Us8412-0yA__"),
  @("N35 Nature - Weave\round 1", "n35r1-04_display-on-oak-desk-in-dark-tropical-forest-dusk-lite.jpg", "https://s3-alpha-sig.figma.com/img/973c/38b9/fe0dd6ac4516f3e424c9f3608085967d.jpg?Expires=1796601600&Key-Pair-Id=APKAQ4GOSFWCW27IBOMQ&Signature=rR7c0GLpIKyGuAdJm6WFXvPUtJrAkkf~HJuZaokbTth05epf0y0VgtxOeIL~YW6glmn-KK48FYzrJaEHX6qktjqz3JI3Orb2C-0XxJWIDdPM-C2fnN05D2bmufYuulVTS05dwY3Ku0qFwqqu0OhI2~7d2QWSpduqVsa2rnvg~KHth3q5uQNEYmRfUl844OfCdOUCcIjr7wtD~NM2BF3MMJiaFbwH-wTBpquM8QobkLc5zkUwShD48uxsvBrl7XJz7EwVgJAtO5IPKCaS7NU8TcwLLyAvpNhi7fYKOBcf6MjEmS5-kj6Xe~JICuDVn0NoFFo6vm4gcAndm8Nr-hUqCg__"),
  @("N35 Nature - Weave\round 1", "n35r1-05_poster-board-on-oak-easel-white-sand-dunes-lite.jpg", "https://s3-alpha-sig.figma.com/img/4e7e/0f80/51969b3a19e81e1343f61c25496eefba.jpg?Expires=1796601600&Key-Pair-Id=APKAQ4GOSFWCW27IBOMQ&Signature=IPaGU6y-nHAgQLNy~KwV93tJLavSAPk6qu-5hZ5KgBX8WTeJsdYU5btnyS-Pr5rM6Ro~cYywuaBWPyrK3aIKaFx-zldJg-tt-4QUtXrFTaLTFTO-hwAGkdhrn8Ey2p8Bp6DDta9OKl8ktdB9bBPcsqpx2cyM5X1AmQHMS7~-1v3svYd44oI~vHqsy5RLnCNQYm~1ju83SaufwpxYsDQrvqWGIVEAE0HrLgSXyfjXeL1Oq~Rf3beDHdjdXuqqheskvbI93b8fYAsV7IArnBfbhHwjJLyYRhvzdXdiWqZfE-6AiEh3T7BAKO47N8AdO~bps6Z-dFZz1OaR9W0Bk3boEA__")
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
