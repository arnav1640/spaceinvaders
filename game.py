
########################################
#        -Space Invader-               #
#   Author: Arnav Gaddam version 1     #
#                                      #
#   description: OOP Space Invaders    #
# with pygame                          #
#                                      #
#                                      #
########################################


import pygame
import pygame.time

from objects.load_assets import defender_ship, invader_ship, background_img
from objects.ship import Ship
from objects.defender import Defender
from objects.enemies import Enemies
from objects.invader import Invader

WIDTH = 800
HEIGHT = 800

background = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SPACE INVADERS")
ship = Defender(500, 700)
enemies = Enemies(
    [Invader(100, 100), Invader(200, 100), Invader(300, 100), Invader(400, 100), Invader(500, 100), Invader(600, 100),
     Invader(700, 100),
     Invader(150, 170), Invader(250, 170), Invader(350, 170), Invader(450, 170), Invader(550, 170), Invader(650, 170),
     Invader(100, 240), Invader(200, 240), Invader(300, 240), Invader(400, 240), Invader(500, 240), Invader(600, 240),
     Invader(700, 240)])
ship.enemies = enemies.invaders

pygame.font.init()
# font = pygame.font.Font('freesansbold.ttf', 32)
font2 = pygame.font.SysFont('didot.ttc', 72)
img2 = font2.render('GAME OVER', True, (68, 189, 189))


def menu():
    # screen.fill((0, 0, 0))
    active = 1
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
        screen.blit(img2, (250, 300))
        pygame.display.update()





def gameloop():
    clock = pygame.time.Clock()
    active = True
    elapsed_time = 0
    state = 1
    while active:
        clock.tick(264)
        screen.blit(background, (0, 0))
        timepast = clock.tick()
        elapsed_time += timepast
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and ship.x - ship.velocity > 0:  # left
            ship.move("left")
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and ship.y + ship.velocity < HEIGHT:  # left
            ship.move("down")
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and ship.x + ship.velocity < WIDTH:  # left
            ship.move("right")
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and ship.y - ship.velocity > 0:  # left
            ship.move("up")
        if keys[pygame.K_SPACE] or keys[pygame.K_RETURN]:  # left
            ship.shoot()
        if elapsed_time > 200:
            elapsed_time = 0
            # for enemyship in enemies.invaders:
            #     enemyship.shift()



        ship.update(screen, enemies.invaders)
        enemies.update(screen)
        enemycooldown = 300

        pygame.display.update()
        if len(enemies.invaders) == 0:
            break


gameloop()
menu()
pygame.quit()
