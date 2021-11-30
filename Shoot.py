import pygame

class shoot(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("Data/tiro.png")
        self.image = pygame.transform.scale(self.image, [30, 30])
        self.rect = pygame.Rect(self.image.get_rect())

        self.speed = 7

    def update(self, *args):
        self.rect.x +=  self.speed