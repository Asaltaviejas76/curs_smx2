function Mostrar-Mensaje {
    param([string]$Texto = "Mensaje por defecto")
    Write-Host $Texto
}
Mostrar-Mensaje
Mostrar-Mensaje "Hola desde la función"
