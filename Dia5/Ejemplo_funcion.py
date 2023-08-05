precios_cafe = [("capuchino",1.5),("Expreso",1.2),("Moka",1.9)]

def cafe_mas_caro(lista_precios):

    precio_mayor = 0
    cafe_mas_caro = ""

    for cafe,precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass
    return cafe_mas_caro,precio_mayor

cafe,precio = cafe_mas_caro(precios_cafe)

print(f"el cafe mas caro es {cafe} cuyo precio es {precio}")
