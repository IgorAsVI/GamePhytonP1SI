import pygame


class Guy (pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.rect = pygame.Rect(50, 50, 100, 100)
        self.image = pygame.image.load("Data/KINGChar.png")
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.speed = 0
        self.speedy = 0
        self.aceleration = 0.2

    def update(self, *args):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speed -= self.aceleration
        elif keys[pygame.K_RIGHT]:
            self.speed += self.aceleration
        elif keys[pygame.K_UP]:
            self.speedy -= self.aceleration
        elif keys[pygame.K_DOWN]:
            self.speedy += self.aceleration
        else:
            self.speed *=0.95
            self.speedy *= 0.95

        self.rect.x += self.speed
        self.rect.y += self.speedy

        if self.rect.top < 0 :
            self.speedy += self.aceleration * 30
        if self.rect.bottom > 720:
            self.speedy -= self.aceleration * 30


        if self.rect.right > 1080:
            self.speed -= self.aceleration * 30
        if self.rect.left < 0 :
            self.speed += self.aceleration * 30


