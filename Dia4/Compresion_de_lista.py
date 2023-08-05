palabra = "python"

lista = [letra for letra in "python"]

print(lista)

lista = [int(numero / 2) for numero in range(0,21,2)]

print(lista)

lista = [numero if numero *2 >10 else "no"  for numero in range(0,21,2)]

print(lista)

pies = [10,20,30,40]
metros = [pie /3.281 for pie in pies]
print(metros)
