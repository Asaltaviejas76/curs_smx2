param([string]$RutaDirectorio = ".",[string]$Extension = ".txt")
function Comprobar-RutaExiste {
    param([string]$Ruta)
    return (Test-Path $Ruta)
}
function Buscar-ArchivosPorExtension {
    param([string]$Ruta,[string]$Ext)
    return Get-ChildItem -Path $Ruta -File -Recurse | Where-Object { $_.Extension -eq $Ext }
}
if (-not(Comprobar-RutaExiste -Ruta $RutaDirectorio)) { Write-Host "Ruta no existe: $RutaDirectorio"; exit }
$encontrados = Buscar-ArchivosPorExtension -Ruta $RutaDirectorio -Ext $Extension
Write-Host "Cantidad: $($encontrados.Count)"
$encontrados | ForEach-Object { Write-Host $_.FullName }
