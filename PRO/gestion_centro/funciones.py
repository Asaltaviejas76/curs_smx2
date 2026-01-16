import time
from colorama import Fore


def bienvenida(centro):
    print(Fore.YELLOW + "=",Fore.CYAN + "Control Formacion",centro,Fore.YELLOW + "=")
    time.sleep(1)
    print(Fore.YELLOW + "|===========" + Fore.GREEN + " Cargando... " + Fore.YELLOW + "============|")
    time.sleep(1)
    print(Fore.LIGHTBLACK_EX + "|================📎 =================|")

    print(Fore.LIGHTBLACK_EX + "+===", Fore.CYAN + "Bienvenido",centro,Fore.LIGHTBLACK_EX +"====+")
    time.sleep(1)
    print(Fore.YELLOW + "|====================================|")
    print(Fore.YELLOW + "|======= Entrando al sistema ========|")
    print(Fore.YELLOW + "|====================================|")
    print(Fore.YELLOW + "|===========" + Fore.GREEN + " Cargando... " + Fore.YELLOW + "============|")
    print(Fore.YELLOW + "|" + Fore.GREEN + "𝄃𝄂𝄂𝄂𝄂𝄀𝄁𝄃𝄃𝄀𝄁𝄃𝄂𝄂 100% 𝄃𝄂𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃" + Fore.YELLOW + "|")
    print(Fore.YELLOW + "+====================================+")
    time.sleep(1)


def nom18():
    while True:
        nombre = input("Dime nombre y apellidos: ")
        nombre = " ".join(nombre.split())
        if nombre.replace(" ","").isalpha():
            print(Fore.GREEN + "Nombre y apellidos validos:",nombre,"✅")
            break
        else:
            print(Fore.RED + "Error, introduce un nombre valido")


    while True:
        edad = input("Dime tu edad: ")
        if edad.isdigit() and 16 <= int(edad) <= 120:
            print(Fore.GREEN + "Edad valida:",edad,"✅")
            break
        else:
            print(Fore.RED + "Error, introduce un numero valido")


def notas():
    while True:
        n1 = input("Dime nota evaluacon 1: ")
        n1 = n1.replace(",",".")
        if n1.isalpha():
            print(Fore.RED + "Error, introduce un numero valido")

        elif 0 <= float(n1) <= 10:
            break
        else:
            print(Fore.RED + "Error, introduce un numero valido")
    print(Fore.GREEN + "Nota valida:",n1,"✅")

    while True:
        n2 = input("Dime nota evaluacon 2: ")
        n2 = n2.replace(",",".")
        if n2.isalpha():
            print(Fore.RED + "Error, introduce un numero valido")

        elif 0 <= float(n2) <= 10:
            break
        else:
            print(Fore.RED + "Error, introduce un numero valido")
    print(Fore.GREEN + "Nota valida:",n2,"✅")

    while True:
        n3 = input("Dime nota evaluacon 3: ")
        n3 = n3.replace(",",".")
        if n1.isalpha():
            print(Fore.RED + "Error, introduce un numero valido")

        elif 0 <= float(n3) <= 10:
            break
        else:
            print(Fore.RED + "Error, introduce un numero valido")
    print(Fore.GREEN + "Nota valida:",n3,"✅")


def floline(texto):
    print(Fore.CYAN + "+============",texto,"============+")


def asis():
    while True:
        asis = input("Dime tu % de asistencia: ")
        if asis.isdigit() and int(asis) <= 100:
            print(Fore.GREEN + "Asistencia valida:",asis,"✅")
            break
        else:
            print(Fore.RED + "Error, introduce un porcentaje de asistencia valido")


