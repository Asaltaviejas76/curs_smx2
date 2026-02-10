function Crear-Directorio {
    param([string]$Ruta)
    if (-not(Test-Path $Ruta)) { New-Item -ItemType Directory -Path $Ruta | Out-Null }
}
function Crear-Archivo {
    param([string]$Ruta,[string]$Nombre)
    $rutaCompleta = Join-Path $Ruta $Nombre
    if (-not(Test-Path $rutaCompleta)) { New-Item -ItemType File -Path $rutaCompleta | Out-Null }
    return $rutaCompleta
}
function Escribir-ContenidoEnArchivo {
    param([string]$RutaArchivo,[string]$Texto)
    Set-Content -Path $RutaArchivo -Value $Texto
}
Crear-Directorio -Ruta ".\\proyecto"
$archivo = Crear-Archivo -Ruta ".\\proyecto" -Nombre "f16.txt"
Escribir-ContenidoEnArchivo -RutaArchivo $archivo -Texto "Contenido inicial"
Get-Content $archivo | ForEach-Object { Write-Host $_ }
