t = ('C', 'h', 'R', 'm', 'A', 's', 'M', 'o', 'T', 'y', 'c')

mayus = ()
minus = ()

for letra in t:
    if letra.isupper():
        mayus += (letra,)
    else:
        minus += (letra,)

resultado = mayus + minus

print(resultado)
