t = input("Introduce una frase: ")
p = t.split()

print("Las palabras de la frase son:")
for p in p:
    print(p)

print("Número de palabras en la frase:", len(p))