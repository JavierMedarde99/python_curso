from random import *

nombre = input("Dime tu nombre :")
print(f"Buenas {nombre} tienes 8 intento para adivinar el numero")

numero_random = randint(1,100)

for e in range(1,9) :
    numero_usuario = int(input("Adivina el numero :"))
    if numero_usuario <=0 or numero_usuario >100 :
        print("el numero esta comprendido entre el 1 y el 100")
    elif numero_usuario<numero_random:
        print(f"el numero elegido es mayor que el numero puesto ({numero_usuario})")
    elif numero_usuario>numero_random:
        print(f"el numero elegido es menor que el numero puesto ({numero_usuario})")
    else:
        print(f"felicidades Ha acertado el numero, numero de intentos {e}")
        break


