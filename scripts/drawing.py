import random, pygame
'''
    By: Luis Gustavo Caris dos Santos

    Classe visual com resolução dinâmica para pygame
    Todas as informações de tamanho e localização dos objetos serão considerada em porcentagem sobre a tela
'''
class Drawing(pygame.sprite.Sprite):
    def __init__(self, surface):
        # Surface deve ser a superficie em que os objetos serão desenhados
        self.screen = surface
    
    def DrawText(self, texto, local, size, font='Cortana', cor=(255, 255, 255), bold=False, italic=False, antialias=True, reference='topleft'):
        # Desenha um texto na tela, o tamanho da fonte é a porcentagem equivalente a tela e não ao tamanho em pixels
        attributes = ['topleft', 'bottomleft', 'topright', 'bottomright', 'midtop', 'midleft', 'midbottom', 'midright', 'center']
        if reference not in attributes:
            return 'erro'
        self.font = pygame.font.SysFont(font, int(self.screen.get_width()*(size/100)), bold, italic)
        img = self.font.render(texto, antialias, cor)
        img_rect = img.get_rect()
        local_rect = (self.screen.get_width()*(local[0]/100), self.screen.get_height()*(local[1]/100))
        match reference:
            case 'topleft':
                img_rect.topleft = local_rect
            case 'bottomleft':
                img_rect.bottomleft = local_rect
            case 'topright':
                img_rect.topright = local_rect
            case 'bottomright':
                img_rect.bottomright = local_rect
            case 'midtop':
                img_rect.midtop = local_rect
            case 'midleft':
                img_rect.midleft = local_rect
            case 'midbottom':
                img_rect.midbottom = local_rect
            case 'midright':
                img_rect.midright = local_rect
            case 'center':
                img_rect.center = local_rect
        self.screen.blit(img, (img_rect.x, img_rect.y))
        return img_rect

    def DrawImage(self, image, local, size):
        # Desenha uma imagem na tela, deve ser passado uma variavel contendo a imagem e não a pasta em que se encontra
        img = pygame.transform.scale(image, (self.screen.get_width()*(size[0]/100), self.screen.get_height()*(size[1]/100)))
        self.screen.blit(img, (self.screen.get_width()*(local[0]/100), self.screen.get_height()*(local[1]/100)))

    def DrawButton(self, local, size, color=(255, 255, 255), text="", color_text=(0, 0, 0), width=0, image=0, image_size=75, radius=-1, bold=False, italic=False, antialias=True):
        # Desenha um botão na tela e retorna:
        #    [0]Rect do botão
        #    [1][0]se o botão foi clicado
        #       [1]se o mouse ta em cima do botão
        # Pode conter uma imagem ou texto centralizado no botão
        image_local = (local[0]+size[0]*((100-image_size)/2)/100, local[1]+size[1]*((100-image_size)/2)/100)
        image_size = (size[0]*image_size/100, size[1]*image_size/100)
        local = [self.screen.get_width()*(local[0]/100), self.screen.get_height()*(local[1]/100)]
        size = [self.screen.get_width()*(size[0]/100), self.screen.get_height()*(size[1]/100)]
        button_rect = pygame.Rect(*local, *size)
        pygame.draw.rect(self.screen, color, button_rect, width, radius)
        center = [button_rect.center[0]*100/self.screen.get_width(), button_rect.center[1]*100/self.screen.get_height()]
        self.DrawText(text, center, 5, cor=color_text, bold=bold, italic=italic, antialias=antialias, reference='center')
        if image != 0:
            self.DrawImage(image, image_local, image_size)
        return (button_rect, *self.ButtonClick(button_rect))

    def ButtonClick(self, button_rect):
        # Recebe o rect de um botão e retorna:
        #    [0]se o botão foi clicado
        #    [1]se o mouse ta em cima do botão
        mouse_click = mouse_pass = False
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if button_rect.collidepoint(mouse):
            mouse_pass = True
            if click[0]:
                mouse_click = True
        return (mouse_click, mouse_pass)

    def DrawBar(self, local, size, percent=100, color_bar=(255,255,255), color_outline=(255,255,255), radius=-1):
        # Desenha uma barra e retorna:
        #    [0]Rect da barra
        #    [1]Porcentagem de onde a barra foi clicada(a mesma porcentagem recebida se não ouver click)
        local = [self.screen.get_width()*(local[0]/100), self.screen.get_height()*(local[1]/100)]
        size = [self.screen.get_width()*(size[0]/100), self.screen.get_height()*(size[1]/100)]
        percent_rect = pygame.Rect(*local, size[0]*percent/100, size[1])
        bar_rect = pygame.Rect(*local, *size)
        pygame.draw.rect(self.screen, color_bar, percent_rect)
        pygame.draw.rect(self.screen, color_outline, bar_rect, 4, radius)
        return (bar_rect, self.BarClick(bar_rect, percent))

    def BarClick(self, bar_rect, percent):
        # Recebe o rect de uma barra e retorna a porcentagem de onde a barra foi clicada
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if bar_rect.collidepoint(mouse):
            if click[0]:
                return int(((mouse[0]-bar_rect[0])*100)/bar_rect.w)
        return percent

    def DrawStatic(self, static=True, backstatic=True, alpha=50):
        # Cria o efeito de estatica na tela
        img_backstatic = pygame.image.load(f'images/static/{random.randint(12, 19)}.png')
        img_backstatic.set_alpha(alpha)
        img_backstatic = pygame.transform.scale(img_backstatic, (self.screen.get_width(), self.screen.get_height()))
        img_static = pygame.image.load(f'images/static/{random.randint(20, 34)}.png')
        img_static.set_alpha(alpha)
        img_static = pygame.transform.scale(img_static, (self.screen.get_width(), self.screen.get_height()))
        if backstatic:
            self.screen.blit(img_backstatic, (0, 0))
        if static:
            self.screen.blit(img_static, (0, 0))