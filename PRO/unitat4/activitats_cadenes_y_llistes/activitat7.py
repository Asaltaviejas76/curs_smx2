alum=[]
eda=[]

while True:
    inal = input("Dime alumno: ")
    
    if inal == "-":
        break

    ineda = int(input("Dime edad: "))

    alum.append(inal) 
    eda.append(ineda)

print("Alumnos mayores de edad")
for i in range(len(alum)):
    if eda[i] >= 18:
        print(alum[i])