$archivo = "informe.TXT"

switch -Wildcard -CaseSensitive ($archivo)
{
    "*.txt" {"Archivo de texto (.txt)" }
    "*.log" {"Archivo de registro (.log)" }
    }
