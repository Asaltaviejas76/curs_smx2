function Buscar-TextoEnArchivos {
    param([string]$RutaDirectorio,[string]$Patron)
    Get-ChildItem -Path $RutaDirectorio -File -Recurse | ForEach-Object {
        $coincidencias = Select-String -Path $_.FullName -Pattern $Patron -AllMatches -ErrorAction SilentlyContinue
        if ($coincidencias) { $coincidencias | ForEach-Object { Write-Host "$($_.Path):$($_.LineNumber): $($_.Line.Trim())" } }
    }
}
Set-Content -Path ".\\f15_a.txt" -Value "buscar texto ejemplo"
Buscar-TextoEnArchivos -RutaDirectorio "." -Patron "buscar"
