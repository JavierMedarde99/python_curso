class Pajaro:

    alas = True

    def __init__(self,color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print(f'pio, mi color es {self.color}')
    
    def volar(self,metros):
        print(f'el pajaro ha volado {metros} metros')
        self.piar()
    
    def pintar_negro(self):
        self.color = 'negro'
        print(f"Ahora el pajaro es {self.color}")

    @classmethod
    def poner_huevo(cls,cantidad):
        print(f"puso {cantidad} de huevos")
        cls.alas = False

    @staticmethod
    def mirar():
        print("el pajaro mira")

piolin = Pajaro('amarillo','canario')
piolin.pintar_negro()
piolin.volar(50)
piolin.alas = False
print(piolin.alas)

Pajaro.poner_huevo(3)
print(Pajaro.alas)

Pajaro.mirar()