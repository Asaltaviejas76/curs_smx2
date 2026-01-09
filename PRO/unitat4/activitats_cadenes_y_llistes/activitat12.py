animales = "gato, perro, canario, pescado, conejo, hámster"

lista_animales = animales.split(", ")

resultado = ()

for animal in lista_animales:
    resultado += ((animal, len(animal)),)

print(resultado)
