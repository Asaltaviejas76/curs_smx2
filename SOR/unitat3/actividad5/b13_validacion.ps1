do {
    $tex = Read-Host "dime algo (no puede estar vacio)"
} while ([string]::IsNullOrWhiteSpace($tex))

"es valido"
