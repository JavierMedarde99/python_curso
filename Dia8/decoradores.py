
def cambiar_letras(tipo):
    def mayusculas(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())

    if tipo == "may":
        return mayusculas
    else:
        return minuscula

def una_funcion(funcion):
    return funcion

mi_funcion = cambiar_letras("may")

mi_funcion("python")

una_funcion(mi_funcion("probando"))


def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print("hola")
        funcion(palabra)
        print("adios")
    return otra_funcion


def mayusculas(texto):
    print(texto.upper())
@decorar_saludo
def minusculas(texto):
    print(texto.lower())

mayusculas_decorada = decorar_saludo(mayusculas)

mayusculas("Fede")
mayusculas_decorada("fede")
minusculas("FEDE")