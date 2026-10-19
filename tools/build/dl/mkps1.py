"""Write get-roundNN.ps1: python3 mkps1.py <out.ps1> <folder> <name|url> ..."""
import sys
out,folder,pairs=sys.argv[1],sys.argv[2],sys.argv[3:]
L=['$ErrorActionPreference = "Continue"','$base = "C:\\Users\\38349\\Desktop\\01"','$items = @(']
rows=[]
for p in pairs:
    n,u=p.split('|',1); rows.append(f'  @("{folder}", "{n}.png", "{u}")')
L.append(',\n'.join(rows)); L+=[')','$ok=0; $have=0; $fail=0',
'foreach ($it in $items) {','  $dir = Join-Path $base $it[0]','  New-Item -ItemType Directory -Force -Path $dir | Out-Null',
'  $dst = Join-Path $dir $it[1]','  if (Test-Path $dst) { $have++; continue }','  $done=$false',
'  for ($i=1; $i -le 3 -and -not $done; $i++) {','    try { Invoke-WebRequest -Uri $it[2] -OutFile $dst -UseBasicParsing; $done=$true; $ok++ }',
'    catch { Start-Sleep -Seconds 2 }','  }','  if (-not $done) { $fail++; Write-Host "Failed: $($it[1])" }','}',
'Write-Host "Done. $ok images, $have already there, $fail failed."']
open(out,'w',newline='\r\n').write('\n'.join(L)+'\n')
