try:
    amigos = ["Ana", "Luis", "Carlos", "María"]

    indice = int(input(f"Elige un índice (0-{len(amigos)-1}): "))
    print(f"Tu amigo es: {amigos[indice]}")
except ValueError:
    print("[ERROR] Solo se aceptan numeros")
except IndexError:
    print("[ERROR] Numero fuera de rango")