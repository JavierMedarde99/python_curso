mi_archivo = open('/home/javi/python/curso/Python/Dia6/prueba.txt',"r")

print(mi_archivo.readline().rstrip())

print(mi_archivo.readline().upper())

print(mi_archivo.readline())

for line in mi_archivo:
    print('Aqui dice' + line)

todas = mi_archivo.readlines()
print(todas)





mi_archivo.close()