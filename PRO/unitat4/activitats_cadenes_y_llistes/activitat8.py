nombres = []
horas = []
totalextras = []

while True:
    nombre = input("Dime nombre del trabajador: ")

    if nombre == "-":
        break

    hora = int(input("Dime horas extra mes: "))

    nombres.append(nombre)
    horas.append(hora)

for i in range(len(horas)):
    total = horas[i] * 16.25
    totalextras.append(total)

print("Dinero por horas extra: ")
for i in range(len(nombres)):
    print(nombres[i], "-", totalextras[i], "€")
