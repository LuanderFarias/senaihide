import pygame
from pygame.locals import *
from sys import exit
from pygame._sdl2 import Window
import os

pygame.init()

largura = 300
altura = 300

windowx = 0
windowy = 0

playerx = largura/2
playery = altura/2
velocidade = 10
clock = pygame.time.Clock()

tela = pygame.display.set_mode((largura, altura), pygame.RESIZABLE)
pgwindow = Window.from_display_module()
pgwindow.position = (windowx, windowy)
pygame.display.set_caption('Senaihide')

while True:
    clock.tick(60)
    tela.fill((255,255,255))
    comandos = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if comandos[pygame.K_w]:
        print("W precionado")
        playery -= velocidade
    if comandos[pygame.K_s]:
        print("S precionado")
        playery += velocidade
    if comandos[pygame.K_d]:
        print("D precionado")
        playerx += velocidade
        pgwindow.position = (windowx+10, 0)
    if comandos[pygame.K_a]:
        print("A precionado")
        playerx -= velocidade
    if comandos[pygame.K_f]:
        pygame.display.toggle_fullscreen()
    
    pygame.draw.rect(tela, (255,0,0), (playerx,playery,50,50)) # edjalma
    pygame.display.update()
