nombres = ["Ana","Hugo", "Valeria"]
edades = [65,29,42]
ciudades = ["Lima","Madrid","Mexico"]

combinado = list(zip(nombres,edades,ciudades))

for nombre,edad,ciudad in combinado:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")

print(combinado)
