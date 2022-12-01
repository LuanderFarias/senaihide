from game import Game
from configparser import ConfigParser, ExtendedInterpolation

config = ConfigParser(interpolation=ExtendedInterpolation())
config.read('data/config.conf')

dimensao  = config['DEFAULT']['resolution'].split('x')
g = Game(dimensao, config['DEFAULT']['screen'])

while g.running:
    g.curr_menu.display_menu()
    g.game_loop(),