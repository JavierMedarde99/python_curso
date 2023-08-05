mi_lista = ["a","b","c"]
mi_lista2 = ["d","e","f"]
mi_lista3 = mi_lista + mi_lista2
otra_lista = ["hola",55,6.2]
print(type(mi_lista))
print(len(mi_lista))
print(mi_lista[0:])
print(len(mi_lista3))

mi_lista3[0] = "alfa"
mi_lista3.append("g")
elimindo = mi_lista3.pop(0)

print(mi_lista3)
print(elimindo)


lista = ["g", "o", "b", "m", "c"]
lista.sort()
print(lista)
lista.reverse()
print(lista)

