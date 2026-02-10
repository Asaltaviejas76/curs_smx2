function Operacion-Numeros {
    param([double]$Numero1,[double]$Numero2)
    return ($Numero1 + $Numero2)
}
$resultado = Operacion-Numeros -Numero1 5 -Numero2 3
Write-Host "Resultado: $resultado"
