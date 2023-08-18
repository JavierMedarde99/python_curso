import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance
import pyjokes
import webbrowser
import datetime
import wikipedia

# Escuchar nuestro microfono y devolver el audio como texto 
def trasformar_audio_en_texto():

    # almacenar recognizer en variable
    r = sr.Recognizer()

    # Configurar el microfono
    with sr.Microphone() as origen:

        # tiempo de espera 
        r.pause_threshold = 0.8

        # informar que comenzo la grabacion
        print("ya puedes hablar")

        # guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # buscar en google
            pedido = r.recognize_google(audio, language="es-es")

            # prueba de que pudo ingresar
            print("dijiste: "+ pedido)

            return pedido
        #en caso de que no comprenda el audi
        except sr.UnknownValueError:

            #prueba de que no comprendio el audio
            print("ups no entendi")

            #devolver error
            return "sigo esperando"
        #En caso que no resolver el pedido
        except sr.RequestError:

            return "sigo esperando"
        #error inesperado
        except:

            return "sigo esperando"
        

# funcion para que el asistente hable
def hablar(mensaje):

    #encender el motor de pysttsx3
    engine = pyttsx3.init()

    # pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


# informar dia de la semana
def pedir_dia():

    # Crear la variable con datos de hoy
    dia = datetime.date.today()
    print(dia)

    # Crear una variable para el dia de la semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # diccionario con nombres de dia
    calendario = {0:"Lunes", 1: "Martes",2: "Miercoles",3: "Jueves",4: "Viernes",5:"Sabado",6:"Domingo"}

    #decir dia de la semana
    hablar(f'hoy es {calendario[dia_semana]}')


# Informar que hora es
def pedir_hora():

    # crear una variable con datos de la hora
    hora = datetime.datetime.now()
    print(hora)
    hora = f"En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos"
    # Decir la hora
    hablar(hora)

# funcion saludo inicial
def saludo_inicial():

    #crear variable condatos de hora 
    hora = datetime.datetime.now()

    if hora.hour < 6 or hora.hour>20:
        momento = "Buenas noches"
    elif hora.hour >= 6 and hora.hour < 13:
        momento = "Buen dia"
    else:
        momento = "Buenas tardes"

    # Decir el salido
    hablar(f"{momento} soy Helena, tu asistente personal. Por favor, dime en que puedo ayudar")


# Funcion central del asistente
def pedir_cosas():

    #activar el saludo inicial
    saludo_inicial()

    #variable de corte
    comenzar = True

    #Loop central
    while comenzar:

        #Activar el micro y guardar el pedido en un String
        pedido = trasformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Con gusto, estoy abriendo youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abiri navegador' in pedido:
            hablar('Claro estoy en eso')
            webbrowser.open('https://www.google.com')
            continue
        elif 'que dia es hoy' in pedido:
            pedir_dia()
            continue
        elif 'que hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Buscando eso en wikipedia')
            pedido = pedido.replace('busca en wikipedia','')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido,sentences=1)
            hablar('Wikipedia dice lo sieguente')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Ya mismo estoy en eso')
            pedido = pedido.replace('busca en internet','')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar("buena idea ya comienzo a reproducirlo")
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple': 'APPL', 'amazon': 'AMZN','google': 'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yfinance.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontre, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar("perdon pero no la he encontrado")
                continue
        elif 'adios' in pedido:
            hablar("Me voy a descansar, cualquier cosa me avisas")
            break


pedir_cosas()