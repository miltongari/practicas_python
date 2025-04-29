from string import punctuation

import pygame
import random
import math
from pygame import mixer


# Inicializar pygame
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800,600))

# Titulo e Icono
pygame.display.set_caption("Invasion espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("Fondo.jpg")

# Agregar musica
mixer.music.load("MusicaFondo.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# variables del jugador
player_img = pygame.image.load("cohete.png")
player_x = 368
player_y = 500
player_x_cambio = 0

# Variable de enemigos
enemy_img = []
enemy_x = []
enemy_y =  []
enemy_x_cambio = []
enemy_y_cambio = []
cantidad_enemigos = 16

for e in range(cantidad_enemigos):
    enemy_img.append(pygame.image.load("enemigo.png"))
    enemy_x.append(random.randint(0, 736))
    enemy_y.append(random.randint(50, 200))
    enemy_x_cambio.append(0.2)
    enemy_y_cambio.append(50)

# Variable de la bala
balas = []
bala_img = pygame.image.load("bala.png")
bala_x = 0
bala_y =  500
bala_x_cambio = 0
bala_y_cambio = 1
bala_visible = False

# Puntuaje
puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf', 32)
texto_x = 10
texto_y = 10

# Texto final de juego
fuente_final = pygame.font.Font('freesansbold.ttf', 40)

def text_final():
    mi_fuente_final = fuente_final.render("JUEGO TERMINADO", True,(255,255,255))
    pantalla.blit(mi_fuente_final,(220, 200))

# Funcion mostrar puntuaje
def mostrar_puntuaje(x, y):
    texto = fuente.render(f"Puntuaje: {puntaje}", True, (255,255,255))
    pantalla.blit(texto, (x,y))


# Funcion del jugador
def player(x,y):
    pantalla.blit(player_img, (x,y))

# Funcion del enemigo
def enemy(x,y, ene):
    pantalla.blit(enemy_img[ene], (x,y))


# Funcion disparar balas
def dispara_balas(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(bala_img, (x + 16,y + 10))

# Funcion detectar coliciones
def hay_colicion(x_1, y_1,x_2,y_2):
    distancia = math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False


# loop del juego
run = True
while run:

    #RGB
    #pantalla.fill((230,112,87))

    # Fondo de pantalla
    pantalla.blit(fondo,(0,0))


    #iterar eventos
    for evento in pygame.event.get():

        # Evento cerrar
        if evento.type == pygame.QUIT:
            run = False

        # evento presionar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                player_x_cambio = - 1
            if evento.key == pygame.K_RIGHT:
                player_x_cambio =  1
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound('disparo.mp3')

                if not bala_visible:
                    sonido_bala.play()
                    bala_x = player_x
                    dispara_balas(bala_x, bala_y)

        # Eveneto soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                player_x_cambio =  0

    # Modificar ubicacion del jugador
    player_x += player_x_cambio

    # Mantener dentro de bordes al jugador
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # Modificar ubicacion del enemigo
    for e in range(cantidad_enemigos):

        # Fin del juego
        if enemy_y [e] > 500:
            for k in range(cantidad_enemigos):
                enemy_y[k] = 1000
            text_final()
            break



        enemy_x[e] += enemy_x_cambio[e]

        # Mantener dentro de bordes al enemigo
        if enemy_x[e] <= 0:
            enemy_x_cambio[e] = 0.2
            enemy_y[e] += enemy_y_cambio[e]
        elif enemy_x[e] >= 736:
            enemy_x_cambio[e] = -0.2
            enemy_y[e] += enemy_y_cambio[e]

            # Colision
        colision = hay_colicion(enemy_x[e], enemy_y[e], bala_x, bala_y)
        if colision:
            sonido_colision = mixer.Sound('Golpe.mp3')
            sonido_colision.play()
            bala_y = 500
            bala_visible = False
            puntaje += 1
            enemy_x[e] = random.randint(0, 736)
            enemy_y[e] = random.randint(50, 200)

        enemy(enemy_x[e], enemy_y[e],e)

    # Movimiento bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False
    if bala_visible:
        dispara_balas(bala_x,bala_y)
        bala_y -= bala_y_cambio




    player(player_x, player_y)

    mostrar_puntuaje(texto_x,texto_y)


    # Actualizar
    pygame.display.update()
