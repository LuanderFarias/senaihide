import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480

playerx = largura/2
playery = altura/2
velocidade = 10
clock = pygame.time.Clock()

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Senaihide')

while True:
    clock.tick(60)
    tela.fill((255,255,255))
    comandos = pygame.key.get_pressed()
    if playerx <= 0:
        playerx = largura
    if playery <= 0:
        playery = altura
    if playerx >= largura:
        playerx = 0
    if playery >= altura:
        playery = 0

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.draw.circle(tela, (0,0,120), (300,260), 40)
    pygame.draw.line(tela, (255,255,0), (390,0), (390,600), 5)

    if comandos[pygame.K_w]:
        print("W precionado")
        playery -= velocidade
    if comandos[pygame.K_s]:
        print("S precionado")
        playery += velocidade
    if comandos[pygame.K_d]:
        print("D precionado")
        playerx += velocidade
    if comandos[pygame.K_a]:
        print("A precionado")
        playerx -= velocidade
    
    pygame.draw.rect(tela, (255,0,0), (playerx,playery,50,50)) # edjalma
    pygame.display.update()
