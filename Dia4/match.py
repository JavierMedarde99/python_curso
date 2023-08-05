serie = "N-02"

if serie == "N-01":
    print("Samsung")
elif serie == "N-02":
    print("Nokia")
elif serie == "N-03":
    print("motorola")
else:
    print("no existe este productor")

match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("motorola")
    case _:
        print("no existe este productor")

cliente = {"nombre": "federico", "edad":45, "ocupacion": "instructor"}

pelicula = {"titulo": "Matrix","ficha_tecnica" : {"protagonista": "Keanu Reeves","director": "Lana y Lilly Wachowski"}}

elementos = [cliente, pelicula, "libro"]

for e in elementos:
    match e:
        case {"nombre": nombre, "edad": edad, "ocupacion": ocupacion}:
            print(f"es un cliente, con edad {nombre}, con edad {edad} y la ocupacion {ocupacion}")
        case {"titulo": titulo, "ficha_tecnica" : {"protagonista" : protagonista,"director":director}}:
            print(f"es una pelicula, con titulo {titulo}, con protaginista {protagonista} y con el/los director/es {director}")
        case _:
            print("no se que es esto")
