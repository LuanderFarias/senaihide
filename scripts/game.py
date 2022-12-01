import pygame
from menu import *
from options import OptionsMenu
from credits import CreditsMenu
from drawing import *

class Game():
    def __init__(self, dimensao, w_flag):
        # Cria a janela com base nas configurações salvas
        pygame.init()
        icon = pygame.image.load('icon.ico')
        pygame.display.set_caption("SenaiHide")
        pygame.display.set_icon(icon)
        if w_flag == 'fullscreen':
            w_flag = pygame.FULLSCREEN
        else:
            w_flag = 0
        self.DISPLAY_W, self.DISPLAY_H = int(dimensao[0]), int(dimensao[1])
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)), w_flag)
        # Status do jogo
        self.running, self.playing, self.static = True, False, True
        # Status de botões precionados
        self.UP_KEY, self.DOWN_KEY, self.LEFT_KEY, self.RIGHT_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False, False, False
        # Cores pré definidas
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        # Opções de menu
        self.main_menu = MainMenu(self, self.window)
        self.options = OptionsMenu(self, self.window)
        self.credits = CreditsMenu(self, self.window)
        # Variavel que guarda qual menu está aberto
        self.curr_menu = self.main_menu

    def game_loop(self):
        # Loop enquanto estiver no jogo em si
        while self.playing:
            self.check_events()
            if self.START_KEY:
                # Enter para voltar ao menu (Apaga isso depois)
                self.playing = False
                self.static = True
            self.window.fill(self.BLACK)
            pygame.display.update()
            self.reset_keys()

    def check_events(self):
        # Checa se algum evento está acontecendo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Checa se o botão de sair foi precionado
                self.running, self.playing, self.static = False, False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                # Checa se algum botão do teclado/joystick foi precionado
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE or event.key == pygame.K_ESCAPE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.UP_KEY = True
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.LEFT_KEY = True
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.RIGHT_KEY = True

    def reset_keys(self):
        # Reseta todos os comandos
        self.UP_KEY, self.DOWN_KEY, self.LEFT_KEY, self.RIGHT_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False, False, False