$valor = "externo"
function Mostrar-Alcance {
    $valor = "interno"
    Write-Host "Dentro: $valor"
}
Write-Host "Fuera antes: $valor"
Mostrar-Alcance
Write-Host "Fuera despues: $valor"
