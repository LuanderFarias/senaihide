import pygame
from drawing import *
from configparser import ConfigParser, ExtendedInterpolation

class Menu():
    def __init__(self, game):
        self.game = game
        self.run_display = True
        self.config_conf = ConfigParser(interpolation=ExtendedInterpolation())
        self.config_conf.read('data/config.conf')
        self.language_conf = ConfigParser(interpolation=ExtendedInterpolation())
        self.language_conf.read('data/language.conf')
        self.screen_conf = ConfigParser(interpolation=ExtendedInterpolation())
        self.screen_conf.read('data/screen.conf')

    def blit_screen(self):
        # Atualiza a parte visual dos menus na tela
        static = Drawing(self.tela).DrawStatic()
        pygame.display.update()
        self.game.reset_keys()

    def check_language(self):
        # Checa em qual linguagem o jogo está configurado
        self.lang = self.config_conf['DEFAULT']['language']
        self.language = ConfigParser(interpolation=ExtendedInterpolation())
        self.language.read(f'texts/{self.lang}/txt.conf')

    def search_in_matriz(self, matriz, valor):
        # Função para buscar posição de valor dentro de uma matriz(vetor dentro de vetor)
        for line in matriz:
            for column in line:
                if column == valor:
                    return (matriz.index(line), line.index(column))

class MainMenu(Menu):
    def __init__(self, game, tela):
        # Criando menu inicial
        Menu.__init__(self, game)
        self.tela = tela
        self.mouse = (0, 0)
        self.states = ['newgame', 'continue', 'options', 'credits', 'exit']
        self.state = "newgame"

    def display_menu(self):
        self.check_language()
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.tela.fill(self.game.BLACK)
            self.statesopt, self.buttons = [], []
            
            self.notebook_art = Drawing(self.tela)
            self.notebook_art.DrawImage(pygame.image.load('images/menu/notebook.png'), (0, 25), (100, 100))
            self.notebook_art.DrawImage(pygame.image.load('images/menu/Senaihide.png'), (25, 7.5), (50, 14))

            #Criar todos os textos do menu inicial na variavel self.statesopt com 10% de altura de diferença entre cada
            for textos in self.states:
                #Usando a variavel self.states como molde para criar os textos
                self.statesopt.append(Drawing(self.tela))
                self.buttons.append(self.statesopt[self.states.index(textos)].DrawText(self.language['MENU'][textos], (35, 35+(self.states.index(textos)*10)), 6))
            self.check_mouse()
            self.draw_cursor()
            self.blit_screen()

    def draw_cursor(self):
        #Carrega imagem da seta de seleção
        cursor_img = pygame.image.load('images/menu/450.png')
        cursor = Drawing(self.tela)
        #Desenha a seta na posição y da opção selecionada
        button = self.buttons[self.states.index(self.state)]
        cursor.DrawImage(cursor_img, (27, (button.y*100)/self.tela.get_height()), (5, 5))

    def move_cursor(self):
        # Muda a localização em que o cursor será desenhado, caso seja ativa a função de click pra baixo ou pra cima
        if self.game.DOWN_KEY:
            if self.states.index(self.state)+1 > len(self.state):
                self.state = self.states[0]
            else:
                self.state = self.states[self.states.index(self.state)+1]
        elif self.game.UP_KEY:
            if self.states.index(self.state) == 0:
                self.state = self.states[-1]
            else:
                self.state = self.states[self.states.index(self.state)-1]

    def check_input(self):
        # Checa se e qual opção foi selecionada
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'newgame' or self.state == 'continue':
                self.game.static = False
                self.game.playing = True
            elif self.state == 'options':
                self.game.curr_menu = self.game.options
            elif self.state == 'credits':
                self.game.curr_menu = self.game.credits
            elif self.state == 'exit':
                self.game.running = False
            self.run_display = False

    def check_mouse(self):
        # Checa se o mouse passou em cima de alguma opção e se ouve um click
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for i in self.buttons:
            if i.collidepoint(mouse):
                if mouse != self.mouse:
                    self.state = self.states[self.buttons.index(i)]
                if click[0]:
                    self.game.START_KEY = True
                    self.check_input()
        self.mouse = mouse