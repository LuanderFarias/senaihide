import pygame
from pygame.locals import *
from sys import exit
from pygame._sdl2 import Window
import os

pygame.init()

width = 400
height = 400

windowx = 0
windowy = 0

playerx = width/2
playery = height/2
speed = 10

clock = pygame.time.Clock()

mwidth, mheight = pygame.display.Info().current_w, pygame.display.Info().current_h

screen = pygame.display.set_mode((width, height), pygame.RESIZABLE, pygame.NOFRAME)
pgwindow = Window.from_display_module()
pgwindow.position = (windowx, windowy)
monitor = pygame.display.Info()
pygame.display.set_caption('Redimension')

while True:
    clock.tick(60)
    screen.fill((225,225,225))
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if width <= mwidth and keys[pygame.K_d]:
        print("right")
        playerx += speed
        width = width+10
        screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        pygame.display.update()
    if width <= 0 and keys[pygame.K_a]:
        print("left")
        playerx -= speed
        width = width-10
        screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        pygame.display.update()
    if height <= 0 and keys[pygame.K_w]:
        print("up")
        playery -= speed
        height = height-10
        screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        pygame.display.update()
    if height <= mheight and keys[pygame.K_s]:
        print("down")
        playery += speed
        height = height+10
        screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        pygame.display.update()
    
    pygame.display.flip()

    pygame.draw.rect(screen, (255,0,0), (playerx,playery,50,50))
    pygame.display.update()
