import pygame


class Ship:

    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = pygame.transform.scale(img, (64, 64))
        self.velocity = 5

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def move(self, direction):
        if direction == "up":
            self.y -= self.velocity
        elif direction == "down":
            self.y += self.velocity
        elif direction == "left":
            self.x -= self.velocity
        elif direction == "right":
            self.x += self.velocity
