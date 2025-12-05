na = input("Dime Nombre y Apellidos: ")
e = input("Dime Edad: ")
t = input("Dime Telefono: ")
n = input("Dime Nickname: ")

esp = na.split()
num = len(esp)
tnum = len(t)

print("--------------------")
print("INFORME GENERAL")
print("--------------------")

while True:
    if num == 3:
        print("Nombre y Apellidos: ")
        for a in esp:
            print(a.capitalize())
        break
    else:
        print("No es es valido el nombre")
        break

while True:
    if e.isdigit():
        print("Edad: ", e)
        break
    else:
        print("No es es valida la edad")
        break

while True:
    if tnum == 9:
        print("Telefono: ", t)
        break
    else:
        print("No es valido el numero de telefono")
        break

while True:
    if n.isalnum:
        print("Nickmame: ", n)
        break
    else:
        print("No es valido el nickname")
        break