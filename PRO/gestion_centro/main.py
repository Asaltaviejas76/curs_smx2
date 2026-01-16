import time
import sys
import math
from colorama import init, Fore, Back, Style

init(autoreset=True)

#Parte 1

from funciones import bienvenida

bienvenida("CIPFP Luis Suñer")

#Parte 2

from funciones import nom18,notas

nom18()

notas()

#Parte 3

from funciones import floline,asis

floline("Asistencia")

asis()

floline("Resultado")

med = (float(n1) + float(n2) + float(n3)) / 3

if int(med) <5 or int(asis) <85:
    print(Fore.RED + "Suspendido ❌")
else:
    print(Fore.GREEN + "Aprobado ✅")

floline("Promocion")

promociona = False

if int(med) <5 or int(asis) <85:
    promociona = False
    print(Fore.RED + "+===== El alumn@ NO Promociona ======+")
else:
    promociona = True
    print(Fore.GREEN + "+======= El alumn@ Promociona =======+")

#Parte 4
print(Fore.YELLOW + "|====================================|")
print(Fore.YELLOW + "|===========" + Fore.GREEN + " Cargando... " + Fore.YELLOW + "============|")
time.sleep(2)
print(Fore.YELLOW + "|" + Fore.GREEN + "𝄃𝄂𝄂𝄂𝄂𝄀𝄁𝄃𝄃𝄀𝄁𝄃𝄂𝄂 100% 𝄃𝄂𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃" + Fore.YELLOW + "|")
time.sleep(2)
print(Fore.YELLOW + "+====================================+")
time.sleep(2)

print(Fore.CYAN + "|=========== INFOME FINAL ===========|")

if int(edad) <= 18:
    print(Fore.CYAN + "|===== Edad:",edad,"-> Menor de edad",Fore.CYAN + "=====|")
else:
    print(Fore.CYAN + "|======== Edad:",edad,"-> Adulto",Fore.CYAN + "========|")
    
print(Fore.CYAN + "|=== Nota:",n1,",",n2,",",n3,Fore.CYAN + "|",round(med,2),Fore.CYAN + "===|")
print(Fore.CYAN + "|========== Asistencia:",asis,Fore.CYAN + "==========|")
print(Fore.CYAN + "+======== ¿Promociona?:",promociona,Fore.CYAN + "========+")