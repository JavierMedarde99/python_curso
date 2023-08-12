mi_lista = [1,1,1,1,1,1]

print(len(mi_lista))

class Objeto:
    pass

mi_objeto = Objeto()
print(mi_objeto)

class CD:

    def __init__(self,autor,titulo,canciones):
        self.autor = autor
        self.titulo=titulo
        self.caciones =canciones

    def __str__(self):
        return f"Album : {self.titulo} de {self.autor}"

    def __len__(self):
        return self.caciones
    
    def __del__(self):
        print("Se ha eliminado el cd")

mi_cd = CD('Pink Flow',"The Wall",24)

print(len(mi_cd))

del mi_cd