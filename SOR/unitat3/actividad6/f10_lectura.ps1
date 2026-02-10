function Leer-Archivo {
    param([string]$RutaArchivo)
    Get-Content -Path $RutaArchivo | ForEach-Object { Write-Host $_ }
}
Set-Content -Path ".\\f10_a.txt" -Value "Archivo A linea"
Set-Content -Path ".\\f10_b.txt" -Value "Archivo B linea"
Leer-Archivo -RutaArchivo ".\\f10_a.txt"
Leer-Archivo -RutaArchivo ".\\f10_b.txt"
