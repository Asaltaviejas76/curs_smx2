param(
    [string]$usu,
    [string]$ruta
)

$contador = 0
$seguir = $true
$mensaje = "Gestion simple de archivos"

if (-not $usu -or -not $ruta) {
    "Faltan parametros"
    exit
}

if (-not (Test-Path $ruta)) {
    "La ruta no existe"
    exit
}

"Usuario: $usu"
"Ruta: $ruta"

while ($seguir) {

    "1 - Ver archivos"
    "2 - Buscar por nombre"
    "3 - Salir"

    $op = Read-Host "Elige opcion"

    switch -Regex ($op) {

        "^1$" {
            "archivos:"
            Get-ChildItem $ruta | Select-Object -ExpandProperty Name
            $contador++
        }

        "^2$" {
            $pat = Read-Host "escribe parte del nombre"
            Get-ChildItem $ruta | Where-Object { $_.Name -match $pat } | Select-Object -ExpandProperty Name
            $contador++
        }

        "^3$" {
            "saliendo..."
            $seguir = $false
        }

        Default {
            "opcion incorrecta"
        }
    }
}

for ($i = 1; $i -le 2; $i++) {
    "creando resumen..."
}

"RESUMEN FINAL"
"Usuario: $usu"
"Ruta usada: $ruta"
"Acciones realizadas: $contador"
"Mensaje: $mensaje"
"Fin del script."