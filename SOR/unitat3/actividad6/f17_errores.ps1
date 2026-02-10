function Comprobar-Directorio {
    param([string]$RutaDirectorio)
    if (-not(Test-Path $RutaDirectorio)) { Write-Host "Error: no existe $RutaDirectorio"; return }
    $archivos = Get-ChildItem -Path $RutaDirectorio -File
    Write-Host "Archivos en $RutaDirectorio: $($archivos.Count)"
    $archivos | ForEach-Object { Write-Host $_.Name }
}
Comprobar-Directorio -RutaDirectorio ".\\no_existe"
Comprobar-Directorio -RutaDirectorio "."
