diccionario = {"c1": "valor1","c2":"valor2"}
print(diccionario)

resultado = diccionario["c1"]
print(resultado)

cliente = {"nombre": "juan", "apellido":"Fuentes", "peso": 88,"talla":1.76}
consulta = cliente["talla"]
print(consulta)

dic = {"c1": 55, "c2": [20,30,40], "c3": {"s1":100,"s2":200}}
print(dic["c3"]["s2"])

dic = {"c1": ["a","b","c"],"c2" : ["d","e","f"]}
print(dic["c2"][1].upper())

dic = {"c1":"a","c2":"b"}
dic[3] = "c"
print(dic)
dic["c2"] = "B"
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())
