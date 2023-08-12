class Animal:

    def __init__(self,edad,color):
        self.edad = edad
        self.color = color


    def nacer(self):
        print("este animal ha nacido")

    def hablar(self):
        print("este animal ha hecho un sonido") 

class Pajaro(Animal):

    def __init__(self, edad, color,altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print("pio")

    def volar(self,metros):
        print(f"el pajaro ha volado {metros}, metros")

print(Pajaro.__bases__)
print(Animal.__subclasses__)

mi_animal = Animal(5,"negro")

piolin = Pajaro(2,"amarillo",60)

piolin.nacer()
piolin.hablar()



class Padre:
    def hablar(self):
        print("Hola")

class Madre:
    def reir(self):
        print("ja ja")

    def hablar(self):
        print("que tal")

class Hijo(Padre,Madre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()

mi_nieto.hablar()

mi_nieto.reir()