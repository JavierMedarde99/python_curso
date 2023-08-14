import zipfile
import os
import re
import datetime
import timeit


def extraer_instrucciones():
    zip_abierto = zipfile.ZipFile('./Dia9/Proyecto+Dia+9.zip', 'r')

    zip_abierto.extractall('./Dia9')

#extraer_instrucciones()

def arbol_directorio(directorio):
    lista_final = []
    for carpeta,subcarpeta,archivo in os.walk(directorio):
        for arch in archivo:
                if arch.endswith(".txt"):
                    lista_final.append(buscar_serie(arch,carpeta))
    return lista_final

def buscar_serie(archivo,carpeta):
    lista_numero_serie = []
    archivo_abierto = open(carpeta+"/"+archivo)
    patron = r'\D{4}-\d{5}'
    texto = archivo_abierto.read()
    numero_serie = re.search(patron,texto)
    if numero_serie != None:
        numero_serie= re.findall(patron,texto)
        lista_numero_serie.append([archivo,numero_serie[0]])
    return lista_numero_serie
     
def tiempo():
    declaracion = '''
arbol_directorio('./Dia9/Mi_Gran_Directorio')
''' 
    mi_setup = '''
import zipfile
import os
import re
import datetime
import timeit

def arbol_directorio(directorio):
    lista_final = []
    for carpeta,subcarpeta,archivo in os.walk(directorio):
        for arch in archivo:
                if arch.endswith(".txt"):
                    lista_final.append(buscar_serie(arch,carpeta))
    return lista_final

def buscar_serie(archivo,carpeta):
    lista_numero_serie = []
    archivo_abierto = open(carpeta+"/"+archivo)
    patron = r'\D{4}-\d{5}'
    texto = archivo_abierto.read()
    numero_serie = re.search(patron,texto)
    if numero_serie != None:
        numero_serie= re.findall(patron,texto)
        lista_numero_serie.append([archivo,numero_serie[0]])
    return lista_numero_serie
'''
    return timeit.timeit(declaracion,mi_setup)


lista_numero_serie = arbol_directorio('./Dia9/Mi_Gran_Directorio')

fecha = datetime.datetime.today()

print(f'''
Fecha de búsqueda: {fecha}

ARCHIVO		NRO. SERIE
-------		----------''')
for lista in lista_numero_serie:
    for values in lista:
        print(f"{values[0]}\t{values[1]}")

    

print(f'''Números encontrados: {len(lista_numero_serie)}
Duración de la búsqueda: {tiempo()} segundos
''')
