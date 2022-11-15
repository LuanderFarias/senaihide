import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480

playerx = largura/2
playery = altura/2

clock = pygame.time.Clock()

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Senaihide')

while True:
    clock.tick(60)
    tela.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        pygame.draw.rect(tela, (255,0,0), (playerx,playery,50,50)) # edjalma
        playerx = playerx - 5
        if playerx <= 0:
          playerx = largura
        pygame.draw.circle(tela, (0,0,120), (300,260), 40)
        pygame.draw.line(tela, (255,255,0), (390,0), (390,600), 5)
        pygame.display.update()
