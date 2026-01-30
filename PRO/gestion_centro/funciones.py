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

def nom():
    while True:
        nombre = input("Dime nombre y apellidos: ")
        nombre = " ".join(nombre.split())
        if nombre.replace(" ","").isalpha():
            print(Fore.GREEN + "Nombre y apellidos validos:",nombre,"✅")
            return nombre
        else:
            print(Fore.RED + "Error, introduce un nombre valido")

def ed():
    while True:
        edad = input("Dime tu edad: ")
        if edad.isdigit() and 16 <= int(edad) <= 120:
            print(Fore.GREEN + f"Edad válida: {edad} ✅")
            return int(edad)
        print(Fore.RED + "Error, introduce una edad válida")

def notaev(num):
    while True:
        nota = input(f"Dime nota evaluación {num}: ").replace(",", ".")
        try:
            nota = float(nota)
            if 0 <= nota <= 10:
                print(Fore.GREEN + f"Nota válida: {nota} ✅")
                return nota
        except ValueError:
            pass
        print(Fore.RED + "Error, introduce un número válido")

def floline(texto):
    print(Fore.CYAN + "+============",texto,Fore.CYAN + "============+")

def asis():
    while True:
        asis = input("Dime tu % de asistencia: ")
        if asis.isdigit() and 0 <= int(asis) <= 100:
            print(Fore.GREEN + f"Asistencia válida: {asis}% ✅")
            return int(asis)
        print(Fore.RED + "Error, introduce un porcentaje válido")

def cargline():
    print(Fore.YELLOW + "+====================================+")
    print(Fore.YELLOW + "|===========" + Fore.GREEN + " Cargando... " + Fore.YELLOW + "============|")
    time.sleep(2)
    print(Fore.YELLOW + "|" + Fore.GREEN + "𝄃𝄂𝄂𝄂𝄂𝄀𝄁𝄃𝄃𝄀𝄁𝄃𝄂𝄂 100% 𝄃𝄂𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃" + Fore.YELLOW + "|")
    time.sleep(2)
    print(Fore.YELLOW + "+====================================+")
    time.sleep(2)