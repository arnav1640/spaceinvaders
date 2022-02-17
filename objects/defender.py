import pygame
from objects.ship import Ship
from objects.load_assets import defender_ship
from objects.bullet import Bullet

class Defender(Ship):

    def __init__(self, x, y):
        super().__init__(x, y, defender_ship)
        self.fired = False

    def shoot(self):
        self.bullets.append(Bullet(self.x, self.y))

    def update(self, screen, tracker):
        screen.blit(self.img, (self.x, self.y))
        for bullet in self.bullets:
            bullet.update(screen)
        
        

