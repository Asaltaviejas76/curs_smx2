function Sobrescribir-Archivo {
    param([string]$RutaArchivo,[string]$Texto)
    if (Test-Path $RutaArchivo) { Write-Host "Antes:"; Get-Content $RutaArchivo | ForEach-Object { Write-Host $_ } }
    Set-Content -Path $RutaArchivo -Value $Texto
    Write-Host "Despues:"; Get-Content $RutaArchivo | ForEach-Object { Write-Host $_ }
}
Set-Content -Path ".\\f09.txt" -Value "Contenido antiguo"
Sobrescribir-Archivo -RutaArchivo ".\\f09.txt" -Texto "Contenido nuevo"
