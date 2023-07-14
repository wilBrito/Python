import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
import pyaudio


id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'

# escuchar microfono y devolver el audio como texto
def transformar_audio_en_texto():

    #almacenar recognizer en variable
    r = sr.Recognizer()

    #configuar el microfono
    with sr.Microphone() as origen:

        # tiempo de espera
        r.pause_threshold = 0.8

        # informar que empezo la grabación
        print('Ya puede hablar')

        # guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # buscar en google
            pedido = r.recognize_google(audio, language='es-es')

            # prueba de que pudo ingresar
            print('Dijiste: ' + pedido)

            # devolver a pedido
            return pedido

        # en caso de que no comprende el audio
        except sr.UnknownValueError:
            print('ups, no entendi')

            return 'sigo esperando'

        except sr.RequestError:
            print('ups, no hay servicio')

            return 'sigo esperando'

        except:
            print('ups, algo ha salido mal')

            return 'sigo esperando'


# funcion para que el asistente pueda ser escuchado
def hablar(mensaje):

    #enceder el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id)

    #pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


def pedir_dia():

    # crear variable con datos de hoy
    dia = datetime.datetime.today()

    #crear variable para dia de semana
    dia_semana = dia.weekday()

    #diccionario con nombre de dias
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domingo'}

    #decir el dia de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')


def pedir_hora():

    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos '
    hablar(hora)


def saludo_inicial():

    hora = datetime.datetime.now()

    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buenos días'
    else:
        momento = 'Buenas tardes'

    hablar(f'{momento}, soy Maxine, tu asistente personal. Por favor, dime en que te puedo ayudar')


def pedir_cosas():
    saludo_inicial()

    comenzar = True

    while comenzar:
        pedido = transformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Con gusto, estoy abriendo youTube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Claro, estoy en eso')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'buscar en wikipedia' in pedido:
            hablar('Buscando eso en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siguiente:')
            hablar(resultado)
        elif 'busca en internet' in pedido:
            hablar('Ya mismo estoy en eso')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('Genial ya comienzo a reproducirlo')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple': 'APPL', 'amazon': 'AMZN', 'google': 'GOOGL'}

            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontre en precio de {accion} es {precio_actual}')
                continue
            except:
                hablar('Perdón no la he encontrado')
        elif 'adiós' in pedido:
            hablar('Me voy a descansar, cualquier cosa me avisas')
            break


pedir_cosas()




