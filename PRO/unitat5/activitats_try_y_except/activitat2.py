try:
    num1 = float(input("Primer número: "))
    num2 = float(input("Segundo número: "))
    operacion = input("Operación (+, -, *, /): ")
    if operacion == '+':
        print(num1 + num2)
    elif operacion == '-':
        print(num1 - num2)
    elif operacion == '*':
        print(num1 * num2)
    elif operacion == '/':
        print(num1 / num2)
except ValueError:
    print("[ERROR] Solo se aceptan numeros")
except ZeroDivisionError:
    print("[ERROR] No se puede dividir entre cero")