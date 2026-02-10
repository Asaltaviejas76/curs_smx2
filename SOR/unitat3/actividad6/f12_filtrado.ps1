function Filtrar-PorExtension {
    param([string]$RutaDirectorio,[string]$Extension)
    Get-ChildItem -Path $RutaDirectorio -File | Where-Object { $_.Extension -eq $Extension } | ForEach-Object { Write-Host $_.Name }
}
New-Item -ItemType File -Path ".\\f12_a.log" | Out-Null
New-Item -ItemType File -Path ".\\f12_b.txt" | Out-Null
Filtrar-PorExtension -RutaDirectorio "." -Extension ".txt"
