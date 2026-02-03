$texto = Read-Host "Introduce un valor"

switch -Regex ($texto)
{
    '^[0-9]+$'        {"Solo numeros." }
    '^[a-zA-Z]+$'     {"Solo letras." }
    '^[a-zA-Z0-9]+$'  {"Mezcla de letras y numeros." }
    }
