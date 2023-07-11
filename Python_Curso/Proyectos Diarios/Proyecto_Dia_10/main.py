import pygame
import random
import math
from pygame import mixer
import io


# Inicializar Pygame
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Título e Icono
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load("images/ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("images/Fondo.jpg")

# Agregar musica
mixer.music.load("music/MusicaFondo.mp3")
mixer.music.set_volume(0.4)
mixer.music.play(-1)

# Variables Jugador
img_jugador = pygame.image.load("images/cohete.png")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0


# Variables enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

# Fuente byte
def fuente_byte(fuente):
    with open(fuente, 'rb') as f:
        ttf_bytes = f.read()
    return io.BytesIO(ttf_bytes)


for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("images/enemigo.png"))
    enemigo_x.append(random.randint(0,736))
    enemigo_y.append(random.randint(50,200))
    enemigo_x_cambio.append(0.2)
    enemigo_y_cambio.append(50)


# Variables bala
balas = []
img_bala = pygame.image.load("images/bala.png")
bala_x = 0
bala_y = 500
bala_y_cambio = 1
bala_visible = False

# Puntaje
puntaje  = 0
fuente_como_byte = fuente_byte("font/FreeSansBold.ttf")
fuente = pygame.font.Font(fuente_como_byte, 32)
#fuente = pygame.font.Font("freesansbold.ttf", 32)
texto_x = 10
texto_y = 10

# texto fin de juego
fuente_final = pygame.font.Font(fuente_como_byte, 40)
#fuente_final = pygame.font.Font("freesansbold.ttf", 40)





# Funcion texto final
def texto_final():
    mi_fuente_final = fuente_final.render("JUEGO TERMINADO", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (200, 200))


# funcion mostrar puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (texto_x, texto_y))


# Funcion Jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# Funcion Enemigo
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))

# Funcion disparar bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))

# Funcion colisiones
def colisiones(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_2 - x_1,2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False


# Loop del juego
se_ejecuta = True
while se_ejecuta:

    # RGB
    #pantalla.fill((205, 144, 228))
    pantalla.blit(fondo,(0,0))

    # Iterar eventos
    for event in pygame.event.get():

        # Evento cerrar
        if event.type == pygame.QUIT:
            se_ejecuta = False

        # Evento precionar flecha
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                jugador_x_cambio = -0.4
            if event.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.4

            if event.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound("music/disparo.mp3")
                sonido_bala.play()
                nueva_bala = {
                    "x": jugador_x,
                    "y": jugador_y,
                    "velocidad": -1
                }
                balas.append(nueva_bala)
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

        # Evento soltar flecha
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                jugador_x_cambio = 0


    # Modificar posición del jugador
    jugador_x += jugador_x_cambio

    # Mantener dentro del borde al jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # Modificar posición del enemigo
    for e in range(cantidad_enemigos):

        #fin del juego
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break

        enemigo_x[e] += enemigo_x_cambio[e]

    # Mantener dentro del borde al enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.2
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.2
            enemigo_y[e] += enemigo_y_cambio[e]

        # colision
        for bala in balas:
            colision_bala_enemigo = colisiones(enemigo_x[e], enemigo_y[e], bala["x"], bala["y"])
            if colision_bala_enemigo:
                sonido_colision = mixer.Sound("music/Golpe.mp3")
                sonido_colision.play()
                balas.remove(bala)
                puntaje += 1
                enemigo_x[e] = random.randint(0, 736)
                enemigo_y[e] = random.randint(20, 200)
                break

        enemigo(enemigo_x[e], enemigo_y[e], e)

    # Movimiento bala
    for bala in balas:
        bala["y"] += bala["velocidad"]
        pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 10))
        if bala["y"] < 0:
            balas.remove(bala)
    for bala in balas:
        bala["y"] += bala["velocidad"]
        pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 10))
        if bala["y"] < 0:
            balas.remove(bala)




    jugador(jugador_x, jugador_y)

    mostrar_puntaje(texto_x, texto_y)


    # Actualizar
    pygame.display.update()