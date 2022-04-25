from sprite import *
from kivy.clock import Clock
from random import *
#O, PROSZE, TUTAJ JEST TILE ZE ZSUPEROWANYM SOURCEM, TO POWINNO OCZYSCIC KOD TILI
class L2Tile(Sprite):
    def __init__(self, pos):  # przywoluje w konstruktorze pozycje,CHYBA NIE JEST WYKORZYSTYWANA
        super(L2Tile, self).__init__(source='img/id ltile 2.png')

    def update(self):  # apdejt klasy
        self.x -= 2
        if self.x < -300:  # przeniescu tutaj podobne liczny do przesuwania podlogi
            self.x = 1000  # scrollujego
            self.y = randint(120, 200)
            self.x = randint(1000, 1950)  # jak sie




