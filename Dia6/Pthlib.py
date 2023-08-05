from pathlib import Path

carpeta = Path('/home/javi/python/curso/Python/Dia6/prueba.txt')

print(carpeta.read_text())

print(carpeta.name)

print(carpeta.suffix)

print(carpeta.stem)

if not carpeta.exists():
    print('Este archivo no existe')
else:
    print('genial, existe')