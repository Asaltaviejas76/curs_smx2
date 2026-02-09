$tex = "holayearyAdios76Mano777Arroz"

$let = 0
$num = 0

for ($i = 0; $i -lt $tex.Length; $i++) {
    $caracter = $tex[$i]
    
    if ([char]::IsLetter($caracter)) {
        $let++
    }
    elseif ([char]::IsDigit($caracter)) {
        $num++
    }
}

"letras: $let"
"numeros: $num"
