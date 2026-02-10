function Escribir-EnArchivo {
    param([string]$RutaArchivo,[string]$Texto)
    Set-Content -Path $RutaArchivo -Value $Texto
}
Escribir-EnArchivo -RutaArchivo ".\\f07.txt" -Texto "Primera linea"
Escribir-EnArchivo -RutaArchivo ".\\f07.txt" -Texto "Segunda linea"
Write-Host "Contenido final:"
Get-Content ".\\f07.txt" | ForEach-Object { Write-Host $_ }
