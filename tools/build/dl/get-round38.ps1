$ErrorActionPreference = "Continue"
$base = "C:\Users\38349\Desktop\01"
$items = @(
  @("N37 Night Square - Weave\round 8", "n37r8-01_fresh-tyre-tracks-snowy-avenue-giant-screen.png", "https://blobs.figma.com/blobs/us/download/figma-alpha/img/403d/f554/4d08daee6172fc8e9ccfde463a139774.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQ4GOSFWC3WM52WPH%2F20261126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261126T000000Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=59929a1c2887e08097547ea3f6486f8ebfa122b0754dd84ddd918399cdbced5b"),
  @("N37 Night Square - Weave\round 8", "n37r8-02_stone-colonnade-drizzle-to-giant-screen.png", "https://blobs.figma.com/blobs/us/download/figma-alpha/img/7182/769a/de88c9d3658210bf8469f0a897b82711.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQ4GOSFWC3WM52WPH%2F20261126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261126T000000Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=f9c66ec801a061392d1d95e3f8c4935715ec589e9649a4d82d4b84fdbde2974e"),
  @("N37 Night Square - Weave\round 8", "n37r8-03_waterfront-screen-mirrored-in-still-river.png", "https://blobs.figma.com/blobs/us/download/figma-alpha/img/d1bd/fa0f/198e6113457992b5b9bfd2c100960f4b.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQ4GOSFWC3WM52WPH%2F20261126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261126T000000Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=fd5b035e8bb5b222515e899f7cc8b9a9d46db28199c72c4c8b06f06c22e3456c"),
  @("N37 Night Square - Weave\round 8", "n37r8-04_giant-screen-above-department-store-glass-doors.png", "https://blobs.figma.com/blobs/us/download/figma-alpha/img/0b71/ebbf/b5a6b73af9b6f45cb6cb5e8427c61dce.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQ4GOSFWC3WM52WPH%2F20261126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261126T000000Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=b5b78566642248be9436baee6d36601a9a31058eae5e71ffa9fbb8c16879faf3"),
  @("N37 Night Square - Weave\round 8", "n37r8-05_long-lens-screen-between-dark-towers-snow.png", "https://blobs.figma.com/blobs/us/download/figma-alpha/img/1ed0/3a54/d3430255773a272d1fd1057be6810089.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQ4GOSFWC3WM52WPH%2F20261126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261126T000000Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=ec46ae62f92cc75ffa11f2a424c80954ca4e6d5a6c8d3453e1cefabeee605233"),
  @("N37 Night Square - Weave\round 8", "n37r8-07_empty-ice-rink-below-giant-screen-snow.png", "https://blobs.figma.com/blobs/us/download/figma-alpha/img/3427/9eca/e308de4ee8833c2784065c4b09bbfecf.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQ4GOSFWC3WM52WPH%2F20261126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261126T000000Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=d9021c147a605394c912b84205eda2159338c20a0c9611eddadc6fac9b07b151"),
  @("N37 Night Square - Weave\round 8", "n37r8-08_shuttered-shops-below-giant-screen-drizzle.png", "https://s3-alpha-sig.figma.com/img/9b44/8fd7/1451a3e712e2df094858df9703a1842d.png?Expires=1796601600&Key-Pair-Id=APKAQ4GOSFWCW27IBOMQ&Signature=ptcGwb6AIoTtf-V0AM8HoN7IXu1Y5QMEbFZBcGGVn0aFmmzAf0rigRPpOepbWfjNFv977qE44DMh2w6SYKec-gxAfuvWuIpEKrLzX2qCQL0GRnIwan57Xkt52Wv63vkYD8DTiXu6VrsvvvuLgrv~OWazSkCL7tzpYrm71Hotv~ZOiphyDNHvtKJT9lq~lGc9jGmffZD3jX7s-NDEsO2-dvMaPAXGrEqk80GPZimfdgBGwnN5Sc5EsFj8q8CinC7WrSVbvB43HWB3wopHpf63-Cjeg7xYm9mA73isOPeVOXj0Ftu9iNN1p7ugLyqRFl5jX752TOHKA5IH~7GP2Yy1TQ__"),
  @("N37 Night Square - Weave\round 8", "n37r8-09_snowy-balcony-railing-to-giant-screen.png", "https://s3-alpha-sig.figma.com/img/2962/2210/b9f365187a2a2cdaca3a01b97b0fe442.png?Expires=1796601600&Key-Pair-Id=APKAQ4GOSFWCW27IBOMQ&Signature=DpCXjQd6xVxxgoXElIxBsET2csWJ4BT3pcCUKYec0jwCVdeADrNtl6JaGZCNcb8js10d~L~D2MiE6NvkYNYPWRXSoW20Mf~p-CndWJwhAi8NpZjVCsDPAsbmwD4F6ofEV7Ky0c-QRIbJUMbwEgoHfBa-CDnwA5OVL1FVGw24DZUC1do7DVKCEjlLx0BTaGqgh9eBNWbRXp-RsQEsIkf7j8VhxlLhNP~Ke8~0saOWDFadbjNqmNPU1eq5BS84bTtXNgagtjutsmqohYZcRwCYMajVP8lO7AB5p3qq1CgB4-A84ilCKkF3Uu0hDhwFvCd2OSOMSrEUgC4KrJLeRCR0JQ__"),
  @("N37 Night Square - Weave\round 8", "n37r8-10_station-canopy-edge-drizzle-to-giant-screen.png", "https://s3-alpha-sig.figma.com/img/45bd/8375/cece4cc725dfdfc725199bb43136a757.png?Expires=1796601600&Key-Pair-Id=APKAQ4GOSFWCW27IBOMQ&Signature=nP~esfmBWS2-AL8GBf9E2eIVCB~PppqocKOajBWDe9-2iRhan861t5XvlKt0cOX8ZNP6aoZrsFMdBbbjeYXUVYnaZMJsI3QgjB27hH01rOyYrMQq0Yjnca4jknsfqvWOreBucwLH5ZDSq02cu9YdBMz5oue9uwSkBFCRzDm2zf9tdz7Y8rT50PxPgDa5vhnX4Miw0nMeXDYwv6ds0xe0Xufq4AdmTPN1yu8Vo9t3SXnT6bXezsFITALKpVyapkdyQdBPXZK9t1z0XIPbwxRHyUJRhikPJan1E6Wu8ew9MfMwu4KRM3gvaXO93XiCzZLum32n3mBVO2ss86-bnrQf6A__")
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
