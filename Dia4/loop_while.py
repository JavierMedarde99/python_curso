monedas = 5

while monedas > 0:
    print(f"tengo {monedas} monedas")
    monedas -= 1
else:
    print("no tengo mas dinero")

respuesta = "s"

while respuesta == "s":
    respuesta = input("quieres seguir? (s/n)")
else:
    print("Gracias")

respuesta = "s"

nombre = input("tu nombre: ")

for letra in nombre:
    if letra == "r":
        break
    print(letra)

nombre = input("tu nombre: ")

for letra in nombre:
    if letra == "r":
        continue
    print(letra)
