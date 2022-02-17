from objects.load_assets import bullet_img
import pygame

class Bullet:

    def __init__(self, initx, inity):
        self.x = initx
        self.y = inity
        self.img = pygame.transform.scale(bullet_img, (16, 32))
        self.active = True

    def update(self, screen):
        if self.active:
            screen.blit(self.img, (self.x+23, self.y-25))
            self.y -= 5
        
        
