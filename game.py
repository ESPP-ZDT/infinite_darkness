from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.label import Label
import random as rnd
from tiles import *
from sprite import *
from background import *
from monsters import *
from hero import *
from kivy.properties import ObjectProperty, NumericProperty, ListProperty

class Menu(Widget):
    def __init__(self):
        super(Menu,self).__init__()
        self.add_widget(Sprite(source='img/the angel.png'))
        self.size = self.children[0].size

    def on_touch_down(self, *ignore):
        parent = self.parent
        parent.remove_widget(self)
        parent.add_widget(Game())


class Game(Widget):
    def __init__(self):#overriduje game
        super(Game ,self).__init__()#overriduje game
        self.game_event_counter = 0 #int liczacy czas w grze

        self.game_over = False
        self.background = Background(source='img/tile 3.png')# przywoluje background, przypisuje do zmiennej
        self.size = self.background.size #ustala size gry na size tilea
        #potem mozna zrobic tile wielkosci ekranu na telefonie
        self.add_widget(self.background)#wyswietla- jak tutaj na dole z tamtymi
        self.hero = Hero(pos= (100, self.height/2))#przywoluje i pozycjonuje bohatera na srodku
        self.add_widget(self.hero)#wyswietla sprite bohatera.



        self.asc_tiles = Asc_Tiles(pos=(rnd.randint(0,1000), rnd.randint(0,100)),size = self.size)#blituje tilesy, musze sprobowac bardziej to zrozumiec
        self.add_widget(self.asc_tiles)#blituje te poruszajace sie do gory tilesy
        self.tile_1 = Tile_1(source='img/i d tile 1.png')#dodaje fat tile,
        self.add_widget(self.tile_1)#i wyswietla

        self.tile_2 = Tile_2(source='img/id tile 4.png')  # dodaje skinny tile,
        self.add_widget(self.tile_2)  # i wyswietla
        self.left_dark = Left_Darkness(source='img/the eraser.png')  # sprowadza erasera
        self.add_widget(self.left_dark)  # blituje go po lewej stronie
        self.right_dark = Right_Darkness(source='img/lord.png')  # sprowadza lorda
        self.add_widget(self.right_dark)  # blituje go po prawej stronie
        self.left_death = Left_Death(source='img/death tile.png')  # sprowadza erasera
        self.add_widget(self.left_death)  # blituje go po lewej stronie
        self.right_death = Right_Death(source='img/death tile.png')  # sprowadza lorda
        self.add_widget(self.right_death)  # blituje go po prawej stronie
        self.floor = Floor_Tile(source='img/tile.png')  # dodaje podloge

        self.add_widget(self.floor)  # i wyswietla
        self.treeman = Treeman(pos=(rnd.randint(-100, 0), rnd.randint(660, 661)))
        self.add_widget(self.treeman)
        self.elephant = Elephant(pos=(rnd.randint(100, 110), rnd.randint(660, 661)))
        self.add_widget(self.elephant)
        #self.add_widget(Sprite(source='img/bladecrab.png'))#przywoluje craba wyswietla

        self.game_over = False
        self.hero_hplabel = Label(center_x=self.center_x, top=self.top - 200, text="0")
        self.add_widget(self.hero_hplabel)
        self.hero_explabel = Label(center_x=self.center_x + 200, top=self.top - 200, text="0")
        self.add_widget(self.hero_explabel)
        self.endgame_label = Label(center=self.center,opacity=0,
                                   text='gameover'+ 'exp'+str(self.hero.experience))
        Clock.schedule_interval(self.update, 1.0 / 60.0)  # ustawia 60 tickow, tempo gry
    def update(self, dt):
        if self.game_over:
            self.game_event_counter = 0
            return
        self.game_event_counter += 1
        if self.game_event_counter >= 300:
            self.tile_1.y += 1

            self.treeman.update()


        if self.game_event_counter >= 500:
            self.elephant.update()


        self.hero_hplabel.text =  'hp'+str(self.hero.hero_hp)
        self.hero_explabel.text='exp'+str(self.hero.experience)


        self.background.update()#updateuje background- kaze mu wykonywac poruszanie
        self.hero.update() # updateuje bohaterac

        self.right_death.update() #updateuje smierc z prawej strony
        self.right_dark.update()  # updateuje erasera
        self.tile_2.update()  # updateuje gruba tile
        self.floor.update() #updateuje podloge
        self.tile_1.update()#updateuje gruba tile
        self.left_death.update() #updateuje smierc z lewej strony
        self.left_dark.update()  # updateuje erasera




        self.asc_tiles.update(dt)#updateuje to ruszajace sie tilesy

        print(self.game_event_counter)


        # z jakiegos powodu nie moge w tym iteratorze animowac.
        for self.asc_tile in self.asc_tiles.children:# iteruje przez liste
            if self.asc_tile.collide_widget(self.hero):#kolizja elementow listy tiki

                self.hero.y = self.asc_tile.asc_tile_1.top#umiesc bohatera na gornej podlodze tile
                self.hero.x += 5  # przesuwa bohatera w prawo
                #self.hero.y += 10
                self.hero.running = True#kaze animacji sie dziac, ale nie dziala
            else:
                self.hero.running = False#

        #MONSTER COLLISIONS WITH OBJECTS
            if self.asc_tile.collide_widget(self.treeman):#przesuwa treemana przy kolizji z asctilem
                self.treeman.x += 5
                self.treeman.floorcoll = True
            else:
                self.treeman.floorcoll = False
            if self.tile_1.collide_widget(self.treeman):  # jesli treeman dotyka tila 1 czyli tego na dole
                self.treeman.x += 5  # przesuwa w prawo
            if self.tile_2.collide_widget(self.treeman):  # jesli treeman dotyka tila 2 czyli tego nagorze
                self.treeman.x += -5  # przesuwa w lewo
            if self.asc_tile.collide_widget(self.elephant):#przesuwa treemana przy kolizji z asctilem
                self.elephant.x += 5
                self.elephant.floorcoll = True
            else:
                self.elephant.floorcoll = False
            if self.tile_1.collide_widget(self.elephant):  # jesli treeman dotyka tila 1 czyli tego na dole
                self.elephant.x += 5  # przesuwa w prawo
            if self.tile_2.collide_widget(self.elephant):  # jesli treeman dotyka tila 2 czyli tego nagorze
                self.elephant.x += -5  # przesuwa w lewo


        #HERO COLLISIONS WITH OBJECTS

        if self.hero.collide_widget(self.tile_2):#kolizja bohatera z tile 2 czyli tagorna
            self.hero.running = True# aktywuje animacje biegu
            self.hero.y = self.tile_2.top#uklada bohatera na gorze tila
            self.hero.x += 4#przesuwa bohatera w prawo z dana predkoscia
            #self.hero.x += 3  # animacj

        elif self.hero.collide_widget(self.tile_1):#kolizja z dolnym grubym tilem
            self.hero.running = True#aktywuje animacje
            self.hero.y = self.tile_1.top#uklada bohatera na gorze tila
            self.hero.x += 3  # przesuwa bohatera w prawo
        elif self.hero.collide_widget(self.floor):#kolizja z podloga
            #self.hero.running = True
            self.hero.y = self.floor.top#uklada na gorze
            self.hero.x -= 10  # przesuwa szybko w lewo
        else:#
            self.hero.running = False#wylacza animacje ruchu



        #HERO COLLISIONS WITH MONSTERS
        if self.hero.collide_widget(self.treeman):#jesli bohater ma kolizje z treemanem
            self.hero.monster_touched = True#aktywuje animacje ataku
            self.treeman.x += 0.2#podbija treemana delikatnie w bok
            self.treeman.y += 2#podbija treemana troszke do gory
            self.treeman.hp += -10
        else:
            self.hero.monster_touched = False#wylacza animacje ataku

        if self.hero.collide_widget(self.elephant):#jesli bohater ma kolizje z treemanem
            self.hero.monster_touched = True#aktywuje animacje ataku
            self.elephant.x += 0.2#podbija treemana delikatnie w bok
            self.elephant.y += 3#podbija treemana troszke do gory
            self.elephant.hp += -8
            print('dostajeszw pipke')
        else:
            self.hero.monster_touched = False#wylacza animacje ataku
        #MONSTER COLLISION WITH HERO

        if self.treeman.collide_widget(self.hero) and self.treeman.dead == False:#jesli treeman dotknie hero
            self.treeman.collision = True#odpala animacje ataku treemana
            self.hero.hero_hp -= self.treeman.sila# #odcina hp u hero
        else:
            self.treeman.collision = False#wylacza animacje ataku i treemana
        #if self.treeman.treeman_dead == False:

        if self.elephant.collide_widget(self.hero) and self.elephant.dead == False:#jesli treeman dotknie hero
            self.elephant.collision = True#odpala animacje ataku treemana
            self.hero.hero_hp -= self.elephant.sila# #odcina hp u hero
        else:
            self.elephant.collision = False#wylacza animacje ataku i treemana
        #if self.treeman.treeman_dead == False:

        #MONSTER DEATH(MOZE TUTAJ DROP?)
        if self.treeman.expdrop == True:
            self.hero.experience += 100
            self.treeman.expdrop = False

        if self.elephant.expdrop == True:
            self.hero.experience += 100
            self.elephant.expdrop = False

        #kolizje warunkujace koniec gry przy dotknieciu prawej oraz lewej czesci ekranu
        if self.hero.collide_widget(self.left_death):
            self.game_over = True

        if self.hero.collide_widget(self.right_death):
            self.game_over = True
        #else
        #print(self.hero.experience)
        #print(self.hero.hero_hp)
        if self.hero.hero_hp <= 0:
            self.game_over = True
            print('game over')
        if self.game_over:
            self.endgame_label.opacity = 1
            #tutaj yy

            self.bind(on_touch_down=self._on_touch_down)

    def _on_touch_down(self, *ignore):
        parent = self.parent
        parent.remove_widget(self)
        parent.add_widget(Menu())



        #nie updateuje podlogi, wiec ona sie nie rusza jak narazie- moze w taki sposob zrobie te krawedzie smierdzace zjadajace bohatera


class GameApp(App):
    def build(self):
        top = Widget()
        top.add_widget(Menu())
        Window.size = top.children[0].size
        return top
        #game = Game()#zmienna overriduje gre
        #Window.size = game.size#nadaje wielkosc okna przez rozmiar gry
        #return game#zwraca gre- tu ja odpala


if __name__ == "__main__":
    GameApp().run()