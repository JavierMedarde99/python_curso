mi_archivo = open('/home/javi/python/curso/Python/Dia6/prueba1.txt',"w")
mi_archivo.write('''hola 
mundo
aqui estoy''')

mi_archivo.writelines(['hola','mundo','aqui','estoy'])



mi_archivo.close()

mi_archivo = open('/home/javi/python/curso/Python/Dia6/prueba.txt',"a")

mi_archivo.write('bienvenido')

mi_archivo.close()