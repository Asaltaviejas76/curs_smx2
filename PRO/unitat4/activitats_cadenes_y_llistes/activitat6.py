m = ["enero", "febrero", "marzo", "abrl", "mayo", "junio","julio", "agosto", "septiembre", "octubre", "noviiembre", "diciembre"]

d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

nm = int(input("Dime numero del mes: "))

print("El mes es:", m[nm - 1])
print("Tiene", d[nm - 1], "días")