from menu import Menu
from drawing import *
from configparser import ConfigParser, ExtendedInterpolation

class OptionsMenu(Menu):
    def __init__(self, game, tela):
        self.tela = tela
        Menu.__init__(self, game)
        self.states = [
            ['music', 'sfx'], 
            ['resolution', 'language'], 
            ['screen', 'joystick'], 
            ['apply', 'back']]
        self.state = 'music'
        self.music_conf = int(self.config_conf['DEFAULT']['music'])
        self.sfx_conf = int(self.config_conf['DEFAULT']['sfx'])
        self.resolution_conf = self.config_conf['DEFAULT']['resolution'].split('x')
        self.resolution_conf = [int(val) for val in self.resolution_conf]
        self.screenmode_conf = self.config_conf['DEFAULT']['screen']
        self.lang_conf = self.config_conf['DEFAULT']['language']
        self.lang_list = self.language_conf['LANGUAGE']['languages'].split('\n')
        self.abbreviations_list = self.language_conf['LANGUAGE']['abbreviations'].split('\n')
        self.language_list = []
        for lang in range(len(self.lang_list)):
            self.language_list.append([self.lang_list[lang], self.abbreviations_list[lang]])
        self.lang_state = self.search_in_matriz(self.language_list, self.lang_conf)[0]
        self.resolutions = self.screen_conf['RESOLUTIONS']['resolutions'].split('\n')
        self.res_state = self.resolutions.index(f'{self.resolution_conf[0]}x{self.resolution_conf[1]}')
        self.screenmode = self.screen_conf['MODE']['modes'].split('\n')
        self.mod_state = self.screenmode.index(self.screenmode_conf)
        self.screenButton = [False, [0, False]]
        self.resolutionButton = [False, [0, False]]
        self.languageButton = [False, [0, False]]

    def display_menu(self):
        self.check_language()
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.tela.fill(self.game.BLACK)
            
            #Opção de volume da música
            self.music_volume = Drawing(self.tela)
            self.music_volume.DrawText(self.language['OPTIONS']['music'], (12, 10), 6.5)
            self.music_conf = self.music_volume.DrawBar((10, 20), (35, 5), int(self.music_conf))[1]
            #Opção de volume dos efeitos sonoros
            self.sfx_volume = Drawing(self.tela)
            self.sfx_volume.DrawText(self.language['OPTIONS']['sfx'], (52, 10), 6.5)
            self.sfx_conf = self.sfx_volume.DrawBar((50, 20), (35, 5), int(self.sfx_conf))[1]
            #Opção de resolução
            self.resolution = Drawing(self.tela)
            self.resolution.DrawText(self.language['OPTIONS']['resolution'], (12, 35), 6.5)
            self.resolutionButton = [self.resolutionButton[1][1], self.resolution.DrawButton((10, 45), (35, 10), text=self.resolutions[self.res_state])]
            self.res_state = self.check_buttonState(self.resolutionButton, self.resolutions, self.res_state)
            #Opção de modo de tela
            self.screen = Drawing(self.tela)
            self.screen.DrawText(self.language['OPTIONS']['screen'], (12, 60), 6.5)
            self.screenButton = [self.screenButton[1][1], self.screen.DrawButton((10, 70), (35, 10), text=self.language['OPTIONS'][self.screenmode[self.mod_state]])]
            self.mod_state = self.check_buttonState(self.screenButton, self.screenmode, self.mod_state)
            #Opção de línguagem
            self.lang = Drawing(self.tela)
            self.lang.DrawText(self.language['OPTIONS']['language'], (52, 35), 6.5)
            self.languageButton = [self.languageButton[1][1], self.lang.DrawButton((50, 45), (35, 10), text=self.language_list[self.lang_state][0])]
            self.lang_state = self.check_buttonState(self.languageButton, self.language_list, self.lang_state)
            #Opção de configurar joystick
            self.joystick_image = pygame.image.load('images/menu/joystick.png')
            self.back = Drawing(self.tela)
            self.back.DrawButton((75, 57.5), (10, 10), image=self.joystick_image)
            #Opção de aplicar
            self.apply = Drawing(self.tela)
            if self.apply.DrawButton((50, 70), (20, 10), text=self.language['OPTIONS']['apply'])[1]:
                self.config_conf['DEFAULT']['language'] = self.language_list[self.lang_state][1]
                self.config_conf['DEFAULT']['sfx'] = str(self.sfx_conf)
                self.config_conf['DEFAULT']['music'] = str(self.music_conf)
                self.config_conf['DEFAULT']['resolution'] = self.resolutions[self.res_state]
                self.config_conf['DEFAULT']['screen'] = self.screenmode[self.mod_state]

                with open('data/config.conf', 'w') as arq:
                    self.config_conf.write(arq)
            #Opção de voltar
            self.back_image = pygame.image.load('images/menu/BlackBack.png')
            self.back = Drawing(self.tela)
            if self.back.DrawButton((75, 70), (10, 10), image=self.back_image)[1]:
                print(self.game.curr_menu)
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            #Texto 'Pode ser necessario reiniciar o jogo para aplicar as mudanças'
            Drawing(self.tela).DrawText(self.language['OPTIONS']['obs'], (10, 85), 2)

            self.draw_cursor()
            self.blit_screen()

    def check_buttonState(self, button, list, state):
        if button[0] == False and button[1][1]:
                if state < len(list)-1:
                    return state + 1
                else:
                    return 0
        else:
            return state

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.START_KEY:
            # TO-DO: Create a Volume Menu and a Controls Menu
            pass

    def draw_cursor(self):
        '''Só copiei do MainMenu,
        vou usar isso pra quando for adicionar comandos de teclado/joystick no menu de opções'''
        #Carrega imagem da seta de seleção
        cursor_img = pygame.image.load('images/menu/450.png')
        cursor = Drawing(self.tela)
        #Desenha a seta na posição y da opção selecionada
        #button = self.buttons[self.states.index(self.state)]
        #cursor.DrawImage(cursor_img, (5, (button.y*100)/self.tela.get_height()), (5, 5))