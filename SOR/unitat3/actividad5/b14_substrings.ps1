$arch = @("documento.txt", "imagen.jpg", "archivo.docx", "script.ps1", "video.mp4")

foreach ($arch in $arch) {
    $index = $arch.LastIndexOf(".")
    
    if ($index -gt 0) {
        $nom = $arch.Substring(0, $index)
        $ext = $arch.Substring($index + 1)
        
        "archivo: $nom extension: $ext"
    }
}
