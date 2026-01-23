from colorama import init, Fore
init(autoreset=True)

#Parte 1

from funciones import bienvenida
bienvenida("CIPFP Luis Suñer")

#Parte 2

from funciones import nom,edad,notaev
nom = nom()
edad = edad()
n1 = notaev(1)
n2 = notaev(2)
n3 = notaev(3)

#Parte 3

from funciones import floline,asis
floline("Asistencia")
asis = asis()

floline("Resultado")
med = (float(n1) + float(n2) + float(n3)) / 3
if int(med) <5 or int(asis) <85:
    print(Fore.RED + "Suspendido ❌")
else:
    print(Fore.GREEN + "Aprobado ✅")

floline("Promocion")
promociona = med >= 5 and int(asis) >= 85
if promociona:
    print(Fore.GREEN + "+======= El alumn@ Promociona =======+")
else:
    print(Fore.RED + "+===== El alumn@ NO Promociona ======+")

#Parte 4

from funciones import cargline
cargline()
print(Fore.CYAN + "|=========== INFOME FINAL ===========|")
if int(edad) <= 18:
    print(Fore.CYAN + "|===== Edad:",edad,"-> Menor de edad",Fore.CYAN + "=====|")
else:
    print(Fore.CYAN + "|======== Edad:",edad,"-> Adulto",Fore.CYAN + "========|")
print(Fore.CYAN + "|=== Nota:",n1,",",n2,",",n3,Fore.CYAN + "|",round(med,2),Fore.CYAN + "===|")
print(Fore.CYAN + "|========== Asistencia:",asis,Fore.CYAN + "==========|")
print(Fore.CYAN + "+======== ¿Promociona?:",promociona,Fore.CYAN + "========+")