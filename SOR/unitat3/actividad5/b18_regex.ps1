$cad = @("ahju", "85944", "mola123", "ARROZ", "aleluya123")

foreach ($cad in $cad) {
    switch -Regex ($cad) {
        '^\d+$' {
            "$cad numeros"
        }
        '^[a-zA-Z]+$' {
            "$cad letras"
        }
        default {
            "$cad mixta"
        }
    }
}
