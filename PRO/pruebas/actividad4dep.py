def ordenar_llista(llista):
    n = len(llista)
    for i in range(n):
        index_minim = i
        for j in range(i + 1, n):
            if llista[j] < llista[index_minim]:
                index_minim = j
        llista[i], llista[index_minim] = llista[index_minim], llista[i]
    return llista

llista = [64, 25, 12, 22, 11]
llista_ordenada = ordenar_llista(llista)
print(f"La llista ordenada es: {llista_ordenada}")