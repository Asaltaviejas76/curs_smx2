$usu = @(
    @{nom="Carlos"; edad=9; rol="usuario"},
    @{nom="Vicente"; edad=29; rol="admin"},
    @{nom="Ruben"; edad=42; rol="admin"},
    @{nom="Maria"; edad=8; rol="usuario"}
)

foreach ($usu in $usu) {
    "$($usu.nom)"
    
    if ($usu.edad -ge 18) {
        "mayor de edad"
    }
    else {
        "menor de edad"
    }
    
    if ($usu.rol -eq "admin") {
        "admin"
    }
    
    if (($usu.edad -ge 18) -and ($usu.rol -eq "admin")) {
        "Ambos"
    }
}
