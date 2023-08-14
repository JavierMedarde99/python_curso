import zipfile
import shutil

#mi_zip = zipfile.ZipFile('./Dia9/archivo_comprimido.zip', 'w')

#mi_zip.write('./Dia9/mi_texto_A.txt')

#mi_zip.write('./Dia9/mi_texto_B.txt')

#mi_zip.close()

#zip_abierto = zipfile.ZipFile('./Dia9/archivo_comprimido.zip', 'r')

#zip_abierto.extractall()

carpeta_origen = '/home/javi/Europa'
archivo_destino = 'Todo_comprimido'
shutil.make_archive(archivo_destino,'zip',carpeta_origen)

shutil.unpack_archive('Todo_comprimido.zip', 'Extraccion Terminada', 'zip')