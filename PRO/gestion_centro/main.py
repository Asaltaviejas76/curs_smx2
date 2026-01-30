from colorama import init, Fore
init(autoreset=True)

#Parte 1

from funciones import bienvenida,nom,ed,notaev,floline,asis,cargline
bienvenida("CIPFP Luis Suñer")

#Parte 2

alumnos = []

while True:
    floline("Nuevo Alumno")
    nombre = nom()
    edad = ed()
    n1 = notaev(1)
    n2 = notaev(2)
    n3 = notaev(3)

#Parte 3

    floline("Asistencia")
    asistencia = asis()

    floline("Resultado")
    med = (float(n1) + float(n2) + float(n3)) / 3

    if int(med) <5 or int(asistencia) <85:
        print(Fore.RED + "Suspendido ❌")
    else:
        print(Fore.GREEN + "Aprobado ✅")

    floline("Promocion")
    promociona = med >= 5 and int(asistencia) >= 85

    if promociona:
        print(Fore.GREEN + "+======= El alumn@ Promociona =======+")
    else:
        print(Fore.RED + "+===== El alumn@ NO Promociona ======+")

    alumnos.append({
        "nombre": nombre,
        "edad": edad,
        "notas": (n1, n2, n3),
        "media": med,
        "asistencia": asistencia,
        "promociona": promociona
        })

    seguir = input("¿Quieres introducir otro alumno? (s/n): ")
    if seguir == "n":
        break

#Parte 4

print("¿Qué quieres hacer?")
print("1. Mostrar TODOS los alumnos")
print("2. Mostrar SOLO un alumno en concreto")

opcion = input("Elige una opción (1/2): ")

if opcion == "1":

    for alumno in alumnos:
        cargline()
        print(Fore.GREEN + f"Alumno: {alumno['nombre']}")

        if int(alumno["edad"]) <= 18:
            print(Fore.CYAN + f"Edad: {alumno['edad']} -> Menor de edad")
        else:
            print(Fore.CYAN + f"Edad: {alumno['edad']} -> Adulto")

        n1, n2, n3 = alumno["notas"]
        print(Fore.CYAN + f"Notas: {n1}, {n2}, {n3} | Media: {round(alumno['media'],2)}")
        print(Fore.CYAN + f"Asistencia: {alumno['asistencia']}%")
        print(Fore.CYAN + f"¿Promociona?: {alumno['promociona']}")
    
elif opcion == "2":

    nombre_buscar = input("Introduce el nombre del alumno que quieres ver: ")
    encontrado = False

    for alumno in alumnos:
        if alumno["nombre"] == nombre_buscar:
            encontrado = True
            cargline()
            print(Fore.GREEN + f"Alumno: {alumno['nombre']}")

            if int(alumno["edad"]) <= 18:
                print(Fore.CYAN + f"Edad: {alumno['edad']} -> Menor de edad")
            else:
                print(Fore.CYAN + f"Edad: {alumno['edad']} -> Adulto")

            n1, n2, n3 = alumno["notas"]
            print(Fore.CYAN + f"Notas: {n1}, {n2}, {n3} | Media: {round(alumno['media'],2)}")
            print(Fore.CYAN + f"Asistencia: {alumno['asistencia']}%")
            print(Fore.CYAN + f"¿Promociona?: {alumno['promociona']}")
            break

    if not encontrado:
        print(Fore.RED + "No se encontró ningún alumno con ese nombre.")

else:
    print(Fore.RED + "Opción no válida.")