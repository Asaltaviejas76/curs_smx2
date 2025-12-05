p1 = input("Dime palabra1: ")
p2 = input("Dime palabra2: ")

while True:
    if p2 == p1:
        print("Las palabras son exactamente iguales")
        break

    p1 = p1.lower()
    p2 = p2.lower()

    if p2 == p1:
        print("Las palabras son iguales")
        break

    if not p2 == p1:
        print("Las palaras son diferentes")
        break