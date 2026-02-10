function Crear-Directorio {
    param([string]$Ruta)
    if (-not(Test-Path $Ruta)) { New-Item -ItemType Directory -Path $Ruta | Out-Null; Write-Host "Directorio creado: $Ruta" } else { Write-Host "Directorio existe: $Ruta" }
}
function Crear-ArchivoEnDirectorio {
    param([string]$Directorio,[string]$Nombre)
    if (-not(Test-Path $Directorio)) { Write-Host "Directorio no existe: $Directorio"; return }
    $rutaCompleta = Join-Path $Directorio $Nombre
    if (-not(Test-Path $rutaCompleta)) { New-Item -ItemType File -Path $rutaCompleta | Out-Null; Write-Host "Archivo creado: $rutaCompleta" } else { Write-Host "Archivo existe: $rutaCompleta" }
}
function Mostrar-ContenidoDirectorio {
    param([string]$Directorio)
    if (-not(Test-Path $Directorio)) { Write-Host "Directorio no existe: $Directorio"; return }
    Get-ChildItem -Path $Directorio | ForEach-Object { Write-Host $_.Name }
}
$ejecutando = $true
$contadorCreados = 0
while ($ejecutando) {
    Write-Host "1) Crear directorio"
    Write-Host "2) Crear archivo"
    Write-Host "3) Mostrar contenido"
    Write-Host "4) Salir"
    $opcion = Read-Host "Elige una opcion"
    switch ($opcion) {
        "1" { $directorio = Read-Host "Nombre directorio"; Crear-Directorio -Ruta $directorio; $contadorCreados++ }
        "2" { $directorio = Read-Host "Directorio"; $nombre = Read-Host "Nombre archivo"; Crear-ArchivoEnDirectorio -Directorio $directorio -Nombre $nombre }
        "3" { $directorio = Read-Host "Directorio"; Mostrar-ContenidoDirectorio -Directorio $directorio }
        "4" { $ejecutando = $false }
        default { Write-Host "Opcion no valida" }
    }
}
Write-Host "Resumen: se han creado $contadorCreados acciones de crear directorio"
