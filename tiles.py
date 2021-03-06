import random as rnd
from sprite import *
from kivy.uix.widget import Widget
#background w troche inny sposob przypisuje obrazek - uzywa do tego zmiennej w klasie - chcialbym moze, zeby tutaj w tych tilach tez zrobic listy, zeby zamiast dokladac
#nowe klasy z tileami, robic listy i zmieniac tile na podstawie booli, albo cos. i z kazdym boolem poruszanie byloby inne, i takie tam - mozna sie pobawic.

class Tile_1(Sprite): #fat small tile
    def update(self): #updateuje klase
        self.x -= 2 #porusza podloga
        if self.x < -300: #przeniescu tutaj podobne liczny do przesuwania podlogi
            self.x = 1000#scrollujego
            self.y = rnd.randint(120, 200)
            self.x = rnd.randint(1000, 1950)#jak sie przesuwa pojawia sie z drugiej strony w innym y
#jak narazie postawowy tile dziala wlasnie tak - ma tylko update, poruszanie wraz z granica - source jest nadawane w game. mozna sprobowac podmienic, dodac supera czy cos. przyrownac
#do potwora, tam zawsze sa jakies rozwiazania.
class Tile_2(Sprite): #slim long tile
    def update(self): #updateuje klase
        self.x -= 10 #porusza podloga
        if self.x < -300: #przeniescu tutaj podobne liczny do przesuwania podlogi
            self.x = 1000#scrollujego
            self.y = rnd.randint(600, 900)#jak sie przesuwa pojawia sie z drugiej strony w innym y
            self.x = rnd.randint(1000, 1300)

#tylko te tile dalej sa dla mnie wielka tajeminica, moze pora obejrzec richarda jonesa ten fragment setke razy, zeby sie tego nauczyc - i moc zastosowac to jakie timed tila, albo cos
#cos ciekawego.
class Asc_Tile(Widget):#Tworzy tile, te takie kwadraciki
    def __init__(self, pos): #w konstruktorza prosi o pozycje
        super(Asc_Tile,self).__init__(pos=pos)#superuje i pozycje tez
        self.asc_tile_1 = Sprite(source = 'img/id tile 2.png')#sprowadza obrazek  podlogi
        self.add_widget(self.asc_tile_1)#adduje tile jako widzet
        self.width = self.asc_tile_1.width# ustawia szerokosc?? jakas jako szerokosc tila a raczej odw, wykorzystane w oryginalnym kodzie, a tutaj nie

    def update(self):#apdejt
        #self.left_spike.y += 2
        self.y += +2 #przesuwa w dol??
        self.asc_tile_1.y = self.y
        self.asc_tile_1.x = self.x
        self.x -= 2 #przesuwa w prawo
        if self.top < 0: #jesli gora tila WIEKSZA NIZ ZERO
            self.parent.remove_widget # TO USUN TILA


class Asc_Tiles(Widget): #GRUPA TILOW
    add_tile = 0#zmienna do dodawania podlog
    def update(self,dt):#apdejt
        for child in list(self.children):#przez liste
            child.update() #apdejtuj poszczegolne tile
        self.add_tile -= dt
        if self.add_tile < 0:
            y = rnd.randint(10, 100) #wymiar w ktorym beda sie pojawiac te tile
            self.add_widget(Asc_Tile(pos =(rnd.randint(0,1000), y)))#koordynaty spawnowania tili, x jest randintem
            self.add_tile = 3 #czestotliwosc spanowania tili


class Floor_Tile(Sprite): #floor tile
    def update(self): #updateuje klase
        if self.x < -10: #przeniescu tutaj podobne liczny do przesuwania podlogi
            self.x = 1000#scrollujego


class Left_Darkness(Sprite): #floor tile
    def update(self): #updateuje klase
        self.x = -530#scrollujego


class Right_Darkness(Sprite): #floor til
    def update(self): #updateuje klase
        self.x = 800#scrollujego


class Left_Death(Sprite): #Tile docelowo przezroczysty, warunkujacy smierc przy dotknieciu lewej czesci ekranu.
    def update(self): #updateuje klase
        self.x = 0#scrollujego


class Right_Death(Sprite): #Tile docelowo przezroczysty, warunkujacy smierc przy dotknieciu lewej czesci ekranu.
    def update(self): #updateuje klase
        self.x = 990#scrollujego


