lista = ["a","b","c","d"]

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"Letra {numero_letra}: {letra}")


lista = ["pablo","laura","luis","julia"]

for nombre in lista :
    if nombre.startswith("l"):
        print(nombre)
    else:
        print("Nombe que no comienza con L")

numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor= mi_valor + numero
print(mi_valor)

palabra = "python"

for letra in palabra:
    print(letra)

for a,b in [[1,2],[3,4]]:
    print(a)
    print(b)

dic = {"clave1" : "a","clave2":"b","clave3":"c"}

for item in dic.values() :
    print(item)
