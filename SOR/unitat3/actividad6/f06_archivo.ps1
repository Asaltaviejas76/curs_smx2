function Ensure-File {
    param([string]$Ruta,[string]$Nombre)
    $rutaCompleta = Join-Path $Ruta $Nombre
    if (-not(Test-Path $rutaCompleta)) { New-Item -ItemType File -Path $rutaCompleta | Out-Null; Write-Host "Creado: $rutaCompleta" } else { Write-Host "Ya existe: $rutaCompleta" }
}
Ensure-File -Ruta "." -Nombre "archivo.txt"
