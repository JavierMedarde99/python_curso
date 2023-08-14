from collections import Counter,defaultdict,namedtuple
numeros = [2,3,4,5,6,7,8,9,43,3]
frase = "al pan pan y al vino vino"
print(Counter(numeros))
print(Counter(frase.split()))

serie = Counter([1,1,1,1,1,1,1,2,2,2,2,3,3,3,4])
print(serie.most_common(2))
print(list(serie))

mi_dic = defaultdict(lambda: 'nada')
mi_dic['uno'] = 'verde'
print(mi_dic['cuatro'])

print(mi_dic)

Persona = namedtuple('Persona',['nombre','altura','peso'])
ariel = Persona('Arie',1.76,79)

print(ariel.altura)