import random 

class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido,numero_cuenta,balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f" el señor/a {self.nombre}, {self.apellido} con el numero de cuenta {self.numero_cuenta}. Su balance es de {self.balance}"  # noqa: E501
    
    def depositar(self,dinero):
        self.balance += dinero
        print("Deposito completado correctamente")

    def retirar(self,dinero):
        if dinero >self.balance:
            print("no puede sacar mas dinero del que tiene en su cuenta actual")
        else:
            self.balance -= dinero
            print("Retirada completado correctamente")

def crearCuenta():
    nombre = input("Ingrese su nombre:")
    apellido = input("Ingrese su apellido:")
    balance_inicial = int(input('Ingrese el balance que desea ingresar en su nueva cuenta:'))  # noqa: E501
    numero_cuenta = random.randint(10000000000000000000,99999999999999999999)
    return Cliente(nombre,apellido,numero_cuenta,balance_inicial)

usuario_de_la_cuenta = crearCuenta()
eleccion = 0
while eleccion !=3:
    print(usuario_de_la_cuenta)
    eleccion = input(""" Eliga una opcion :
            1: depositar dinero
            2: retirar dinero 
            3: salir""")
    match eleccion:
        case "1":
            dinero = int(input("Cunato dinero desea depositar"))
            usuario_de_la_cuenta.depositar(dinero)
        case "2":
            dinero = int(input("Cunato dinero desea retirar"))
            usuario_de_la_cuenta.retirar(dinero)
        case "3":
            break
        case default:  # noqa: F811
            print("eleccion erronea")

    
