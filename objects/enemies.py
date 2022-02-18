

class Enemies:

    def __init__(self, invaders):
        self.invaders = invaders

    def update(self, screen):
        for invader in self.invaders:
            invader.update(screen)