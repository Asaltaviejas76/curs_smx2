$ruta = "C:\Usuarios\yeray\Documentos\informe.pdf"

"Longitud total del texto: $($ruta.Length)"

"Ruta en MAYUSCULAS: $($ruta.ToUpper())"

"Ruta en minusculas: $($ruta.ToLower())"

#Length te dice lo larga que es la ruta,
#ToUpper() sirve para ponerla toda a gritos 
#en mayúsculas para comparar sin líos,
#y ToLower() la deja toda en minúsculas 
#para que todo quede uniforme y no te marees 
#con las mayúsculas.