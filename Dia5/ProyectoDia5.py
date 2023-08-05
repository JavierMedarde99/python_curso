from random import shuffle

lista_palabras = ["hola","patata","juan","pedro"]

letras_no_valiadas = []

vida=6

def elegir_palabra(lista):
    shuffle(lista)
    return lista[0]

def mostrar_palabra(palabra):
    lista = []
    for letras in palabra:
        lista.append("-")
    print(lista)
    return lista

def ver_letra_elegida(letra,palabra,lista):

    for i, letras in enumerate(palabra):
        if letras == letra:
            lista_palabra[i] = letra
    print(lista)
    return lista

def resultado_de_la_jugada(lista,letra):
    if "-" not in lista:
        return 0
    elif letra in lista : 
        return 2
    else:
        return 1

palabra_elegida = elegir_palabra(lista_palabras)

print(palabra_elegida)

lista_palabra =mostrar_palabra(palabra_elegida)

while vida != 0:

    letra =input("Eliga una letra")

    pierde_vida = ver_letra_elegida

    lista_palabra = ver_letra_elegida(letra,palabra_elegida,lista_palabra)

    resultado = resultado_de_la_jugada(lista_palabra,letra)

    match resultado:
        case 0:
            print("has ganado")
            break
        case 1:
            vida -= 1
            print(f"Letra erronea. vidas :{vida}")
        case other:
            print("siga jugando")

if vida == 0:
    print("has perdido")

