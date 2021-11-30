import random

import pygame
from Guy import Guy
from vilao import vilao
from Shoot import shoot

pygame.init()
pygame.display.set_caption("bora lá")
display = pygame.display.set_mode([1080, 720])

gameLoop = True
timer = 45
clock = pygame.time.Clock()

drawGroup = pygame.sprite.Group()
vilaogroup = pygame.sprite.Group()
shootGroup = pygame.sprite.Group()

bg = pygame.sprite.Sprite(drawGroup)
bg.image = pygame.image.load("Data/jose-augusto-cestaro-cenario-castelo (1).png")
bg.image = pygame.transform.scale(bg.image, [1080, 720])
bg.rect = bg.image.get_rect()

guy = Guy(drawGroup)

if __name__ == "__main__":
    while gameLoop:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    newShot = shoot(drawGroup, shootGroup)
                    newShot.rect.center = guy.rect.center
        # dram
        display.fill([10, 140, 34])
        drawGroup.         update()
        timer += 5
        if timer > 30:
            timer = 0
            if random.randint(0, 1) > 0.5:
                newvilao = vilao(drawGroup, vilaogroup)
                print("new")
        colisoes = pygame.sprite.spritecollide(guy, vilaogroup, False  )
        if colisoes:
            print("gameover")
            gameLoop = False

        hits = pygame.sprite.groupcollide(shootGroup,vilaogroup,True,True )


        drawGroup.draw(display)
        pygame.display.update()
