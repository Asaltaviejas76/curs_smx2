try:
    num1 = input("Escribe el primer número: ")
    num2 = input("Escribe el segundo número: ")
    resultado = int(num1) / int(num2)
    print(f"Resultado: {resultado}")
except ValueError:
    print("[ERROR] Solo se aceptan numeros")
except ZeroDivisionError:
    print("[ERROR] No se puede dividir entre cero")