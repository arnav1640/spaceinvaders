import pygame
from objects.load_assets import defender_ship, invader_ship, background_img
from objects.ship import Ship
from objects.defender import Defender

WIDTH = 800
HEIGHT = 800

background = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

screen = pygame.display.set_mode((WIDTH, HEIGHT))

ship = Defender(200, 200)


def gameloop():
    clock = pygame.time.Clock()
    active = True

    while active:
        clock.tick(60)
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and ship.x - ship.velocity > 0:  # left
            ship.move("left")
        if keys[pygame.K_s] and ship.y + ship.velocity < HEIGHT:  # left
            ship.move("down")
        if keys[pygame.K_d] and ship.x + ship.velocity < WIDTH:  # left
            ship.move("right")
        if keys[pygame.K_w] and ship.y - ship.velocity > 0:  # left
            ship.move("up")
        if keys[pygame.K_SPACE]:  # left
            ship.shoot()
        ship.draw(screen)
        pygame.display.update()


gameloop()
pygame.quit()
