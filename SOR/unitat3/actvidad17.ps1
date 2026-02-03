$estado = "bloqueado"

if ($estado -eq "activo")
{
    "El usuario está activo."
    }
elseif ($estado -eq "inactivo")
{
    "El usuario está inactivo."
    }
elseif ($estado -eq "bloqueado")
{
    "El usuario está bloqueado."
    }
else
{
    "Estado no reconocido."
    }
