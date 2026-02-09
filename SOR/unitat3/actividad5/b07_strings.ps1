$arch = @("imagen.jpg", "archivo.txt", "script.ps1", "documento.pdf")

foreach ($arch in $arch) {
    if ($arch -like "*.txt") {
        "$arch es un .txt"
    }
    else {
        "$arch es un formato desconociudo"
    }
}
