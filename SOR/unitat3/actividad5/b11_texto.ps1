$tex = "Texto extremadamente largo para la actividad numero 5 de Borja"

$pal = $tex -split " "

foreach ($pal in $pal) {
    if ($pal.Length -gt 5) {
        $pal
    }
}
