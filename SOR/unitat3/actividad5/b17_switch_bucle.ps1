do {
    $opcion = Read-Host "elije una opcion 1-3"

    $valida = $false

    switch ($opcion) {
        "1" { 
            "has elegido 1"
            $valida = $true
        }
        "2" { 
            "has elegido 2"
            $valida = $true
        }
        "3" { 
            "has elegido 3"
            $valida = $true
        }
        Default { 
            "opcion incorrecta"
        }
    }

} while (-not $valida)
