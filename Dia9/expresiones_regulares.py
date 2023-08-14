import re

texto = "Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"

patron = 'ayuda'

palabra = 'ayuda' in texto
print(palabra)

busqueda = re.findall(patron,texto)

print(busqueda)

for hallazgo in re.finditer(patron,texto):
    print(hallazgo.span())

#print(busqueda.span())

#print(busqueda.start())

#print(busqueda.end())

#print(busqueda.span())

texto = 'llama al 564-525-6588 ya mismo'

patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
resultado = re.search(patron,texto)

print(resultado.group(1))

clave = input("Clave :")
patron = r'\D{1}\w{7}'

chequear = re.search(patron,clave)

print(chequear)

texto = "No atendemos lo lunes por la tarde"

buscar = re.search(r'lunes|martes',texto)
buscar = re.search(r'.....demos',texto)
buscar = re.search(r'^\D',texto)
buscar = re.search(r'^\D$',texto)
buscar = re.findall(r'[^\s]+',texto)
print(buscar)