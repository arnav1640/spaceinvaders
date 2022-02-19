import pygame
from objects.ship import Ship
from objects.load_assets import defender_ship
from objects.bullet import Bullet


class Defender(Ship):

    def __init__(self, x, y):
        super().__init__(x, y, defender_ship)
        self.fired = False
        self.cooldown = 0
        self.enemies = []


    def cooldown_fire(self):
        if self.cooldown >= 40:
            self.cooldown = 0
        elif self.cooldown > 0:
            self.cooldown += 1

    def shoot(self):
        self.cooldown_fire()
        if self.cooldown == 0:
            self.bullets.append(Bullet(self.x, self.y))
            self.cooldown = 1

    def update_bullets(self, screen, enemies):
        self.check_collisions(enemies, screen)
        for bullet in self.bullets:
            bullet.update(screen)

    def check_collisions(self, enemies, screen):
        if len(self.enemies) > 0:
            for enemy in enemies:
                for bullet in self.bullets:
                    if bullet.collision(enemy):
                        print(f"bullet collided with ship at f{bullet.x, bullet.y}")
                        self.bullets.remove(bullet)
                        enemies.remove(enemy)
                    elif bullet.offscreen():
                        self.bullets.remove(bullet)

        for bullet in self.bullets:
            bullet.update(self.screen)

    def update(self, screen, enemies):
        self.screen = screen
        screen.blit(self.img, (self.x, self.y))
        self.update_bullets(screen, enemies)
