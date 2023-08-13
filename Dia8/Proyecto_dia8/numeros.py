def decorador_turno(funcion):
    def turno(palabra):
        print("su turno es:")
        funcion(palabra)
        print("Aguarde y sera atendido")
    return turno

def generar_numero(tipo,numero):
    numero_perfumeria = numero
    numero_farmacia = numero
    numero_drogeria = numero
    while True:
        if tipo == "perfumeria":
            numero_perfumeria +=1
            if numero_perfumeria > 10:
                yield "P-"+str(numero_perfumeria)
            else:
                yield "P-0"+str(numero_perfumeria)
        elif tipo == "farmacia":
            numero_farmacia +=1
            if numero_farmacia > 10:
                yield "F-"+str(numero_farmacia)
            else:
                yield "F-0"+str(numero_farmacia)
            
        else:
            numero_drogeria +=1
            if numero_drogeria > 10:
                yield "D-"+str(numero_drogeria)
            else:
                yield "D-0"+str(numero_drogeria)
            numero_drogeria +=1
