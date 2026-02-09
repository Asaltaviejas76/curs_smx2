$est = @("activo", "inactivo", "bloqueado")

foreach ($est in $est) {
    switch ($est) {
        "activo" {
            "Usuario activo"
        }
        "inactivo" {
            "Usuario inactivo"
        }
        "bloqueado" {
            "Usuario bloqueado"
        }
    }
}
