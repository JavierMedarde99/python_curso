import os
import shutil
#import send2trash

print(os.getcwd())

archivo = open('./Dia9/curso.txt', 'w')
archivo.write('texto de prueba')
archivo.close()

print(os.listdir())


#shutil.move('./Dia9/curso.txt','/home/javi')
#send2trash.send2trash('/home/javi/curso.txt')

print(os.walk('/home/javi'))

for carpeta,subcarpeta,archivo in os.walk('/home/javi'):
    print(f"En la carpeta : {carpeta}")
    print(f"Las subcarpetas son :")
    for sub in subcarpeta:
        print(f"\t{sub}")
    print("Los archivos son:")
    for arch in archivo:
        if arch.startswith('2015'):
            print(f"\t {arch}")
    print("\n")