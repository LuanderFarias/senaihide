import os
import pygame
import random

pygame.init()

FPS = 60 #Frames por segundo
fpsClock = pygame.time.Clock()

#Resolução da tela
largura = 1200
altura = 720

screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("SenaiHide")

#Variaveis do jogo
game_paused = False
menu_local = "new"

#Definição da fonte
font = pygame.font.SysFont("consolas", 50)

#Definição da cor
TEXT_COL = (255, 255, 255)

#Carregar imagens do menu
edjalma_selfie = pygame.image.load(os.path.join('SenaiHide', 'imagens', 'menu', 'Edjalma_selfie.png')).convert_alpha()
seta = pygame.image.load(os.path.join('SenaiHide', 'imagens', 'menu', '450.png')).convert_alpha()

#Escreve na tela
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#Game loop
run = True
inicio = 1
while run:
  screen.fill((0, 0, 0))
  static_back = pygame.image.load(os.path.join('SenaiHide', 'imagens', 'static', f'{random.randint(12, 19)}.png'))
  #2 segundos após abrir o jogo
  if inicio <= 120:
    screen.blit(static_back, (0, 0)) #Estatica de fundo
    inicio += 1
  else:
    #Se não estiver pausado
    static = pygame.image.load(os.path.join('SenaiHide', 'imagens', 'static', f'{random.randint(20, 34)}.png'))
    static_back.set_alpha(80)
    static.set_alpha(80)
    edjalma_selfie = pygame.transform.scale(edjalma_selfie, (700, 700)) #Tamanho da foto do Ejalma

    draw_text("Novo Jogo", font, TEXT_COL, 150, 350)
    draw_text("Continue", font, TEXT_COL, 150, 425)

    if menu_local == "new":
      screen.blit(seta, (90, 360))
    elif menu_local == "continue":
      screen.blit(seta, (90, 435))

    screen.blit(edjalma_selfie, (550, 50)) #Foto do Edjalma no menu
    screen.blit(static_back, (0, 0)) #Estatica de fundo
    screen.blit(static, (0, 0)) #Estatica

  pygame.display.update()
  fpsClock.tick(FPS)
pygame.quit()