function Añadir-Texto {
    param([string]$RutaArchivo,[string]$Texto)
    Add-Content -Path $RutaArchivo -Value $Texto
}
Set-Content -Path ".\\f08.txt" -Value "Linea inicial"
Añadir-Texto -RutaArchivo ".\\f08.txt" -Texto "Linea añadida 1"
Añadir-Texto -RutaArchivo ".\\f08.txt" -Texto "Linea añadida 2"
Write-Host "Contenido final:"
Get-Content ".\\f08.txt" | ForEach-Object { Write-Host $_ }
