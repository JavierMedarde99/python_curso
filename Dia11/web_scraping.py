import bs4
import requests

resultado = requests.get("https://escueladirecta-blog.blogspot.com/")

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

print(sopa.select('title')[0].getText())

parrafo_especial = sopa.select('p')
print(parrafo_especial)

columna_lateral = sopa.select('.content p')
for p in columna_lateral:
    print(p.getText())


# tomar las imagenes de un sitio web

resultado = requests.get('https://www.escueladirecta.com/courses')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

imagenes = sopa.select('.course-box-image')

for i in imagenes:
    print(i['src'])
    imagen_curso = requests.get(i['src'])






