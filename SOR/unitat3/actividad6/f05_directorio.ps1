function Ensure-Directory {
    param([string]$NombreDirectorio)
    if (Test-Path $NombreDirectorio) { Write-Host "Existe: $NombreDirectorio" } else { New-Item -ItemType Directory -Path $NombreDirectorio | Out-Null; Write-Host "Creado: $NombreDirectorio" }
}
Ensure-Directory -NombreDirectorio ".\\prueba_dir"
