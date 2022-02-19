from objects.ship import Ship
import pygame
from objects.load_assets import invader_ship
from objects.load_assets import death_animation

class Invader(Ship):

    def __init__(self, x, y):
        super().__init__(x, y, invader_ship)
        self.state = "alive"
        self.shiftstate = "left"
        self.targ1 = self.x - 80
        self.targ2 = self.x + 80
        self.target = self.x

    def update(self, screen):
        if self.state == "alive":
            screen.blit(self.img, (self.x, self.y))
        elif self.state == "dead":
            screen.blit(death_animation, (self.x, self.y))

    def destroy(self):
        self.state = "dead"

    def shift(self):
        print(self.target)
        if self.x > self.target:
            while self.x > self.target:
                self.x -= 1
            self.target = self.targ2
        if self.x < self.target:
            while self.x < self.target:
                self.x += 1
            self.target = self.targ1


    def shiftleft(self):
        target = self.targ1
        while self.x > target:
            self.x -= 1

    def shiftright(self):
        target = self.targ2
        while self.x < target:
            self.x += 1


