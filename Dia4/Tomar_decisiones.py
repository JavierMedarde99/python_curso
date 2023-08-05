x = 5==2

if x :
    print("es correcto")
else :
    print("no es correcto")


mascota = "perro"

if mascota == "gato":
    print("tienes un gato")
elif mascota == "perro":
    print("tienes un perro")
elif mascota == "pez":
    print("tienes un pez")
else :
    print("No se que animal tienes")

edad = 16
calificacion = 9

if edad < 18 :
    print("eres menor de edad")
    if calificacion >= 7:
        print("Aprobado")
    else:
        print("no Aprobado")
else :
    print("eres adulto")
