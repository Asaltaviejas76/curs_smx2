try:
    saldo = 100
    print(f"Saldo actual: {saldo}€")

    retiro = float(input("¿Cuánto quieres retirar? "))

    assert retiro > saldo
    assert retiro < 0

    saldo -= retiro
    print(f"Retirado: {retiro}€")
    print(f"Nuevo saldo: {saldo}€")
except AssertionError:
    print("[ERROR] No tienes suficiente saldo o has introducido una cantidad negativa")
except ValueError:
    print("[ERROR] Solo se aceptan numeros")