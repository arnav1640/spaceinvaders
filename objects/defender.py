import pygame
from objects.ship import Ship
from objects.load_assets import defender_ship

class Defender(Ship):

    def __init__(self, x, y):
        super().__init__(x, y, defender_ship)

    def shoot(self):
        print("firing")