$archivo = "informe_final.pdf"

$partes = $archivo.LastIndexOf(".")
$archivo.substring($partes)


"Nombre: $($archivo.Substring(0, $partes))"
"Extension: $($archivo.Substring($partes))"