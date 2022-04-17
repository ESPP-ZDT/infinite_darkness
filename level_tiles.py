from sprite import *
from kivy.clock import Clock
from random import *

class L2Tile(Sprite):
    def __init__(self, pos):  # przywoluje w konstruktorze pozycje
        super(L2Tile, self).__init__(source='img/id ltile 2.png')

        #self.y = 10  # nadaje losowa pozycje y treemana
        self.y_border_touched = False #bool obslugujacy dolna i gorna granice
        self.x_border_touched = False #bool obslugujacy prawa i lewa granice


        #Clock.schedule_interval(self.update, .0 / 60.0)

    def update(self):  # apdejt klasy

        self.x -= 2

        if self.x < -300:  # przeniescu tutaj podobne liczny do przesuwania podlogi
            self.x = 1000  # scrollujego
            self.y = randint(120, 200)
            self.x = randint(1000, 1950)  # jak sie




