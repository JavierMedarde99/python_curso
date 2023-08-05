def devolver_letras_no_repetidas(palabra):
    lista_de_letras_unicos = []
    palabra = list(palabra)
    letras_unicas = set(palabra)

    for letra in letras_unicas:
        lista_de_letras_unicos.append(letra)
    lista_de_letras_unicos.sort()
    return lista_de_letras_unicos

print(devolver_letras_no_repetidas("holaaaa"))
