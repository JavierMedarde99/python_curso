from pathlib import Path
from shutil import rmtree
import os

directorio_recetas = Path(Path.home(),"Recetas")

def contar_recetas(directorio):
    cont = 0
    for txt in Path(directorio).glob("**/*.txt"):
        cont += 1
    return cont
    
def elegir_usuario(directorio,carpeta):
    print(f"Las {carpeta}s que hay para elegir son :",end=" ")
    if(carpeta == "categoria"):
        for carpetas in os.listdir(directorio):
            print(carpetas,end=", ")
        print()
    else:
        for txt in Path(directorio).glob("*.txt"):
            print(txt.stem.replace("_"," "),end=", ")
        print()
    categoria_usuario = input(f"Eliga una {carpeta} Anterior : ")
    if carpeta == "receta":
        categoria_usuario = categoria_usuario.replace(" ","_") + '.txt'
    while categoria_usuario not in os.listdir(directorio):
        print("porfavor mire la lista anteriror y elija una")
        categoria_usuario = input(f"Eliga una {carpeta} Anterior : ")
        if carpeta == "receta":
            categoria_usuario = categoria_usuario.replace(" ","_") + '.txt'
    return directorio / categoria_usuario

def leer_archivo(directorio):
    open_directorio = open(directorio)
    return open_directorio.read()

def crear_archivo(directorio,nombre_archivo,contenido_archivo):
    directorio = open(directorio / nombre_archivo,"w")
    directorio.write(contenido_archivo)
    return "Archivo creado correctamente"

def eliminar_archivo(directorio):
    os.remove(directorio)
    return "Archivo eliminado correctamente"

def eliminar_directorio(directorio):
    rmtree(directorio)
    return "Carpeta y todo contendio borrado correctamente"

def opcion_1(directorio):
    directorio = elegir_usuario(directorio,"categoria")
    directorio = elegir_usuario(directorio,"receta")
    leer_archivo(directorio)

def opcion_2(directorio):
    directorio = elegir_usuario(directorio,"categoria")
    nombre_archivo = input("Como quiere que se llame el archivo : ")
    nombre_archivo = nombre_archivo.replace(" ","_") + ".txt"
    print()
    contenido_archivo = input("que contenido quiere para dicho archivo : ")
    return crear_archivo(directorio, nombre_archivo, contenido_archivo)

def opcion_3(directorio):
    categoria_nueva = input("Nombre de la categoria nueva : ")
    categoria_nueva = categoria_nueva.replace(" ","_")
    directorio = directorio / categoria_nueva
    os.mkdir(directorio)
    return "categoria creada correctamente"

def opcion_4(directorio):
    directorio = elegir_usuario(directorio,"categoria")
    directorio = elegir_usuario(directorio,"receta")
    return eliminar_archivo(directorio)

def opcion_5(directorio):
    directorio = elegir_usuario(directorio,"categoria")
    return eliminar_directorio(directorio)

respuesta_usuario = "0"

while respuesta_usuario != "6":

    if(respuesta_usuario=="0"):
        print("Bienvenido a las Recetas de Javi")
    else:
        print("Bienvenido de nuevo a las Recetas de Javi")

    print(f"Las recetas se encunetras ubicadas en {directorio_recetas}")

    print(f"Tienes {contar_recetas(directorio_recetas)}")

    print("""[1] - leer receta
    [2] - crear receta  
    [3] - crear categoría  
    [4] - eliminar receta  
    [5] - eliminar categoría  
    [6] - finalizar programa  """)
        
    respuesta_usuario = input()

    match respuesta_usuario:
        case "1":
            print(opcion_1(directorio_recetas))
        case "2":
            print(opcion_2(directorio_recetas))
        case "3":
            print(opcion_3(directorio_recetas))
        case "4":
            print(opcion_4(directorio_recetas))
        case "5":
            print(opcion_5(directorio_recetas))
        case "6":
            print("Programa finalizado correctamente")
        case other:
            print("Opcion erronea")
            respuesta_usuario = "9"
    os.system("clear")