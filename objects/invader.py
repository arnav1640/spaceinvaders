from objects.ship import Ship
import pygame
from objects.load_assets import invader_ship
from objects.load_assets import death_animation

class Invader(Ship):

    def __init__(self, x, y):
        super().__init__(x, y, invader_ship)
        self.state = "alive"

    def update(self, screen):
        if self.state == "alive":
            screen.blit(self.img, (self.x, self.y))
        elif self.state == "dead":
            screen.blit(death_animation, (self.x, self.y))

    def destroy(self):
        self.state == "dead"

