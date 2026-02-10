function Validar-Positivo {
    param([int]$Numero)
    if ($Numero -gt 0) { return "Valido" } else { return "No valido" }
}
Write-Host (Validar-Positivo -Numero 10)
Write-Host (Validar-Positivo -Numero -5)
