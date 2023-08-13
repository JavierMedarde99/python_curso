import numeros

def principal():
    cont_perf=0
    cont_farma = 0
    cont_drog = 0
    otra_vez = True
    error = False
    while otra_vez:
       
        try:
            eleccion = int(input("""
                    Menu principal:
                    1-perfumeria
                    2-farmacia
                    3-drogeria
        """))
        except :
            print("Vuelve a insertar un valor valido")
        else:
            if eleccion ==1:
                if cont_perf== 0:
                    turno_perf = numeros.generar_numero("perfumeria",0)
                    print(next(turno_perf))
                    cont_perf += 1
                else:
                    print(next(turno_perf))
            elif eleccion == 2:
                if cont_farma== 0:
                    turno_farma = numeros.generar_numero("farmacia",0)
                    print(next(turno_farma))
                    cont_farma +=1
                else:
                    print(next(turno_farma))

            elif eleccion == 3:
                if cont_drog ==0:
                    turno_drog = numeros.generar_numero("drogeria",0)
                    print(next(turno_drog))
                    cont_drog +=1
                else:
                    print(next(turno_drog))
            else:
               print("esa eleccion no se encunetra en nuetro registro porfavor inserte un numero valido")
               error=True

        if not error:
            try:
                otra_vez_eleccion = int(input(""" ¿Otro turno? (1=no, culaquier otro numero = si)"""))
                if otra_vez_eleccion==1:
                    otra_vez=False
            except:
                print("eleccion erronea")


        


principal()