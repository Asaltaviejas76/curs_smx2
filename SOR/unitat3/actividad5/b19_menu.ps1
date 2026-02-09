$salir = $false

while (-not $salir) {

    "1 - Ver datos"
    "2 - Modificar datos"
    "3 - Salir"

    $opcion = Read-Host "Elige una opcion"

    switch ($opcion) {

        "1" {
            "Mostrando datos..."
        }

        "2" {
            "Modificando datos..."
        }

        "3" {
            "Saliendo del menu..."
            $salir = $true
        }

        Default {
            "Opción incorrecta"
        }
    }
}
