def trobar_maxim(llista):
    try:
        maxim = llista[0]
        for element in llista:
            if element > maxim:
                maxim = element
        return maxim
    except IndexError:
        return "La llista esta buida."
    
llista = []
valor_maxim = trobar_maxim(llista)
print(f"El valor màxim és: {valor_maxim}")