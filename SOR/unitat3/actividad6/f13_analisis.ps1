function Analizar-Archivos {
    param([string]$RutaDirectorio)
    Get-ChildItem -Path $RutaDirectorio -File | ForEach-Object {
        $tamano = $_.Length
        $categoria = if ($tamano -lt 1024) { "pequeño" } elseif ($tamano -lt 1048576) { "mediano" } else { "grande" }
        Write-Host "$($_.Name) $tamano $categoria"
    }
}
Set-Content -Path ".\\f13_t.txt" -Value "123"
Analizar-Archivos -RutaDirectorio "."
