function Limpiar-Directorio {
    param([string]$RutaDirectorio,[string]$Extension)
    Get-ChildItem -Path $RutaDirectorio -File -Recurse | Where-Object { $_.Extension -eq $Extension } | ForEach-Object { Remove-Item $_.FullName -Force; Write-Host "Eliminado: $($_.FullName)" }
}
New-Item -ItemType File -Path ".\\f18_del.txt" | Out-Null
Limpiar-Directorio -RutaDirectorio "." -Extension ".txt"
