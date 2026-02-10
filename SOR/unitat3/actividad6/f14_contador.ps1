function Contar-Elementos {
    param([string]$RutaDirectorio)
    $archivos = (Get-ChildItem -Path $RutaDirectorio -File -Recurse).Count
    $subdirectorios = (Get-ChildItem -Path $RutaDirectorio -Directory -Recurse).Count
    Write-Host "Archivos: $archivos"
    Write-Host "Subdirectorios: $subdirectorios"
}
Contar-Elementos -RutaDirectorio "."
