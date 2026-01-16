def suma(a, b, c):
    return print(a+b+c)

def resta(a, b, c):
    return print(a-b-c)

def di_hola(nombre):
    print("Hola", nombre)

def sumalista(numeros):
    total = 0
    for n in numeros:
        total += n
    return print(total)

def sumalistaindiferente(*numeros):
    total = 0
    for n in numeros:
        total += n
    return print(total)
