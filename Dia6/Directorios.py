import os
from pathlib import Path

ruta = '/home/javi/python/curso/Python/Dia6/prueba.txt'

elemento = os.path.basename(ruta)
elemento = os.path.split(ruta)
#ruta = os.makedirs('/home/javi/alternativa/otra')

#os.rmdir('/home/javi/alternativa/otra')

print(elemento)

carpeta = Path('/home/javi/alternativa') / 'otro_archivo.txt'


mi_archivo = open(carpeta)
print(mi_archivo.read())
