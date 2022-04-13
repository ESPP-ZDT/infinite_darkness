from kivy.uix.widget import Widget
from sprite import *

class Background(Widget):#tworzy widzet
    def __init__(self,source):#przywoluje source jako cos gddzie bedzie wstawiany img lub atlas
        super(Background,self).__init__()#superuje ja zeby mozna bylo to uzyc w innych klasach
        self.image = Sprite(source = source)#tworzy zmienna obrazu ktory jest subklasa sprajta
        self.add_widget(self.image)#dodaje obraz jako widzet(?)
        self.size = self.image.size#ustala rozmiar widzeta jako rozmiar obrazuCHYBA
        self.image_dupe = Sprite(source=source, x=self.width)#przywoluje drugi obrazek, z szerokoscia poprzedniego jako pozycja wyswietlajac go po nim
        self.add_widget(self.image_dupe)#wyswietla!! najwyrazniej widzet
    def update(self):
        self.image.x -= 2 #przesuwa pierwszy background w lewo
        self.image_dupe.x -= 2#przesuwa nastepny sprajt tez w lewo

        if self.image.right <= 0: #jesli prawa strona obrazka jest wieksza lub rowna zero(?)
            self.image.x = 0 #ustawia pierwszy obrazek w pierwotnej pozycji
            self.image_dupe.x = self.width #ustawia drugi obrazek w tamtym miejscu gdzie byl