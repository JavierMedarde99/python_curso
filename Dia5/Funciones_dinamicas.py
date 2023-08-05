def chequear_3_cifreas(numero):
    return numero in range(100,1000)

suma = 586 +402

resultado = chequear_3_cifreas(suma)
print(resultado)

def chequear_3_cifreas2(lista):
    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass
    return False

resultado = chequear_3_cifreas2([55,99,60000])
print(resultado)

def chequear_3_cifreas3(lista):

    lista_3_cifras = []

    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras

resultado = chequear_3_cifreas3([55,99,60000,666])
print(resultado)
