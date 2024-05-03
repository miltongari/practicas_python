import pygame
import random

pygame.init()

# var
size = (800, 500)
running = True

# coordenadas player 1
player1_coord_x = 100
player1_coord_y = 100

# coordenadas player 2
player2_coord_x = 700
player2_coord_y = 100

player_speed_y = 0
player2_speed_y = 0

# coordenada de la pelota
pelota_coord_x = 400
pelota_coord_y = 250

pelota_speed_x = random.choice([3,-3])
pelota_speed_y = random.choice([-3,3])


screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # movimiento de player 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_speed_y = -3

            if event.key == pygame.K_s:
                player_speed_y = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_speed_y = 0

            if event.key == pygame.K_s:
                player_speed_y = 0

        # movimiento de player 2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player2_speed_y = -3

            if event.key == pygame.K_DOWN:
                player2_speed_y = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player2_speed_y = 0

            if event.key == pygame.K_DOWN:
                player2_speed_y = 0
    # movimiento de los jugadores
    player1_coord_y += player_speed_y
    player2_coord_y += player2_speed_y

    # movimiento de la pelota
    pelota_coord_x += pelota_speed_x
    pelota_coord_y += pelota_speed_y

    # limitacion de jugador1
    if player1_coord_y > 400:
        player1_coord_y = 400
    elif player1_coord_y < 0:
        player1_coord_y = 0

    # limitacion de jugador2
    if player2_coord_y > 400:
        player2_coord_y = 400
    elif player2_coord_y < 0:
        player2_coord_y = 0



    # rebote de la pelota
    if pelota_coord_y > 500 or pelota_coord_y < 0:
        pelota_speed_y *= -1


    # rebote de puntuacion
    if pelota_coord_x > 789 or pelota_coord_x < 11:
        pelota_coord_x = 400
        pelota_coord_y  = 250
        pelota_speed_x = random.choice([4,-4])
        pelota_speed_y = random.choice([-4,4])
        
    screen.fill("black")

    # player 1
    player1 = pygame.draw.rect(
        screen, "white", (player1_coord_x, player1_coord_y, 15, 100)
    )
    player2 = pygame.draw.rect(
        screen, "white", (player2_coord_x, player2_coord_y, 15, 100)
    )
    pelota = pygame.draw.circle(screen, "white", (pelota_coord_x, pelota_coord_y), 10)

   
    # colicion
    if pelota.colliderect(player1) or pelota.colliderect(player2):
        pelota_speed_x *= -1

    pygame.display.flip()
    clock.tick(60)
    print(clock)
