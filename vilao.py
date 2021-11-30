import math
import random

import pygame


class vilao(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.rect = pygame.Rect(50 , 50 , 100, 100)
        self.image = pygame.image.load("Data/Charvilao.png")
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.aceleracao = 1 + random.random() * 1.5
        self.aceleracao2 = 1.5 + random.random() * 8
        self.speed = 0
        self.speedy = 0
        self.speed -= self.aceleracao * random.randint(1,2)
        self.speedy = self.aceleracao2
        self.timer = 0
        self.rect.x = 1079 + random.randint(1,100)
        self.rect.y = random.randint(2,700)

    def update (self,*args):
        self.timer +=0.01
        self.rect.x += self.speed *0.8
        self.rect.y += self.speedy * 0.8

        if self.rect.right > 1080:
            self.speed -= self.aceleracao *0.1
        if self.rect.left < 0 :
            self.rect.x = 1080

        if self.rect.top < 0 :
            self.speedy += self.aceleracao2
        if self.rect.bottom > 720:
            self.speedy -= self.aceleracao2


