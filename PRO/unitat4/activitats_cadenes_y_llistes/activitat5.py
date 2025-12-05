import random
lista = random.sample(range(1,10),5)

print("U  D  C   M")
for n in lista:
    print(n, n*10, n*100, n*1000)