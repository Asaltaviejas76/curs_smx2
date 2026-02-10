function Listar-Archivos {
    param([string]$RutaDirectorio)
    Get-ChildItem -Path $RutaDirectorio -File | ForEach-Object { Write-Host $_.Name }
}
New-Item -ItemType File -Path ".\\f11_1.txt" | Out-Null
New-Item -ItemType File -Path ".\\f11_2.txt" | Out-Null
Listar-Archivos -RutaDirectorio "."
