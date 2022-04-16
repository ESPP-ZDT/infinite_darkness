from sprite import *
from kivy.clock import Clock
from random import *

class Healing_Heart(Sprite):
    def __init__(self, pos):  # przywoluje w konstruktorze pozycje
        super(Healing_Heart, self).__init__(source='img/id heart.png')

        #self.y = 10  # nadaje losowa pozycje y treemana
        self.y_border_touched = False #bool obslugujacy dolna i gorna granice
        self.x_border_touched = False #bool obslugujacy prawa i lewa granice
        self.healing_amount = randrange(10, 35)

        #Clock.schedule_interval(self.update, .0 / 60.0)

    def update(self):  # apdejt klasy

        self.x += 1

        if self.y_border_touched == True:
            self.y -= 1
        elif self.y_border_touched == False:
            self.y += 1
        else:
            self.y += 0

        if self.y == 930:
            self.y_border_touched = True
        if self.y == -10:
            self.y_border_touched = False

        if self.x == 900:
            self.x += -1
        elif self.x == 100:
            self.x += 1
        else:
            self.x += 0


class Big_Right_Boost(Sprite):#strzalka ktora dodaje charge power herosowi
    def __init__(self, pos):  # przywoluje w konstruktorze pozycje
        super(Big_Right_Boost, self).__init__(source='img/id big rigjt.png')

        #self.y = 10  # nadaje losowa pozycje y treemana
        self.y_border_touched = False #bool obslugujacy dolna i gorna granice
        self.x_border_touched = False #bool obslugujacy prawa i lewa granice
        self.boost_amount = randrange(5, 10)

        #Clock.schedule_interval(self.update, .0 / 60.0)

    def update(self):  # apdejt klasy

        self.x += randrange(1,2)

        if self.y_border_touched == True:
            self.y -= 1
        elif self.y_border_touched == False:
            self.y += 1
        else:
            self.y += 0

        if self.y == 930:
            self.y_border_touched = True
        if self.y == -10:
            self.y_border_touched = False

        if self.x == 900:
            self.x += -1
        elif self.x == 100:
            self.x += 1
        else:
            self.x += 0