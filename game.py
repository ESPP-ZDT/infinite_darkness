from kivy.app import App
from level_tiles import *
from kivy.core.audio import SoundLoader
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
from potions import *
from melee_weapons import *
from kivy.properties import ObjectProperty, NumericProperty, ListProperty

sfx_hit = SoundLoader.load('img/id laugh 1.wav')
class Menu(Widget):
    def __init__(self):
        super(Menu,self).__init__()
        self.add_widget(Sprite(source='img/the angel.png'))
        self.size = self.children[0].size
#CO JAKBY TUTAJ ZROBIC LISTKE SOBIE, Z ROZNYMI OBRAZKAMI, I ONE BY SIE WYSWIETLALY ROZNE?
    def on_touch_down(self, *ignore):
        parent = self.parent
        parent.remove_widget(self)
        parent.add_widget(Game())


class Game(Widget):
    def __init__(self):#overriduje game
        super(Game ,self).__init__()#overriduje game
        self.enemies =[]#lista zawierajaca potwory[NA TYM I TYM POZIOMIE NP]
        self.tiles = [] #lista zawierajaca tile
        self.hearts = []#lista zawierajaca health boosty
        self.charge_boosts = []
        self.bullets = []#lista odpowiadajaca za wyswietlanie z listy odpowiedniej broni - w dalszym rozrachunku.
        self.l2tiles =[]
        self.game_event_counter = 0 #int liczacy czas w grze
        self.game_over = False
        self.background = Background()# przywoluje background, przypisuje do zmiennej
        self.size = self.background.size #ustala size gry na size tilea
        self.add_widget(self.background)#wyswietla- jak tutaj na dole z tamtymi
        self.hero = Hero(pos= (100, self.height/2))#przywoluje i pozycjonuje bohatera na srodku - czy musi tutaj?
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


        for w in self.enemies:#forloop ktory appenduje widzety ktore zostaly dodane w inicie A TO ITERUJE PRZEZ NIA I WRZUCA JE NA EKRAN
            self.add_widget(w)

        for h in self.hearts:#forloop ktory appenduje widzety ktore zostaly dodane w inicie A TO ITERUJE PRZEZ NIA I WRZUCA JE NA EKRAN, MUSI BYC
            self.add_widget(h)

        for b in self.charge_boosts:
            self.add_widget(b)

        for t in self.l2tiles:
            self.add_widget(t)

        for b in self.bullets:
            self.add_widget(b)

        self.add_widget(self.floor)  # i wyswietla
        self.enemies.append(Treeman(pos=(rnd.randint(500, 510), rnd.randint(660, 661)))) #to DODAJE TILE DO LISTY
        self.enemies.append(Elephant(pos=(rnd.randint(500, 510), rnd.randint(660, 661))))
        self.hearts.append(Healing_Heart(pos=(rnd.randint(500, 510), rnd.randint(660, 661))))
        self.sfx_hit = SoundLoader.load('img/random.wav')
        self.game_over = False
        self.hplabel = Label(center_x=self.center_x-100, top=self.top - 200, text="0")
        self.add_widget(self.hplabel)
        self.hero_explabel = Label(center_x=self.center_x + 200, top=self.top - 200, text="0")
        self.add_widget(self.hero_explabel)
        self.endgame_label = Label(center=self.center,opacity=0,
                                   text='gameover'+ 'exp'+str(self.hero.experience))
        Clock.schedule_interval(self.update, 1.0 / 60.0)  # ustawia 60 tickow, tempo gry



    def update(self, dt):
        if self.game_over:
            self.game_event_counter = 0
            return

        self.game_event_counter += 1 #ZACZYNA DODAWAC DO TIMERA- TO POZWALA NA WARUNKOWANIE EVENTOW W GRZE

        self.hplabel.text = 'hp' + str(self.hero.hp)
        self.hero_explabel.text = 'exp' + str(self.hero.experience)

        self.background.update()  # updateuje background- kaze mu wykonywac poruszanie
        self.hero.update()  # updateuje bohaterac
        self.right_death.update()  # updateuje sMierc z prawej strony
        self.right_dark.update()  # updateuje erasera
        self.tile_2.update()  # updateuje gruba tile
        self.floor.update()  # updateuje podloge
        self.tile_1.update()  # updateuje gruba tile
        self.left_death.update()  # updateuje smierc z lewej strony
        self.left_dark.update()  # updateuje erasera

        for enemy in self.enemies:
            if isinstance(enemy,Treeman):
                if self.game_event_counter >= 100:
                    enemy.update()
            elif isinstance(enemy,Elephant):
                if self.game_event_counter >= 100:
                    enemy.update()

        for heart in self.hearts:
            heart.update()

        for boost in self.charge_boosts:
            boost.update()

        for tile in self.l2tiles:
            tile.update()
        
        for bullet in self.bullets:
            bullet.update()
        #instrukcja warunkowa odpalajaca strzelanie z broni - do przerobienia na modul, w klasie broni, z zupelnie innym warunkowaniem - ale to po stworzeniu zebrania dropa i guess
        if self.hero.experience >= 100:
            if (self.game_event_counter % 20) == 0: #ten INT DO MODULO TO MOZE BYC ZMIENNA!!!!! BRONI - JEJ CZESTOTLIWOSC strzelania
                nazwa = Weapon(pos= (self.hero.x,self.hero.y)) #pos bohatera musialbym znalezc albo tutaj, albo odwolujac sie do klasy bohatera w broni.
                self.bullets.append(nazwa)
                self.add_widget(nazwa)

        if (self.game_event_counter%200) == 0:
            nazwa = Treeman(pos=(rnd.randint(0, 1000), rnd.randint(0, 1000)))
            self.enemies.append(nazwa)
            self.add_widget(nazwa)

        if (self.game_event_counter % 90) == 0:
            nazwa = Healing_Heart(pos=(rnd.randint(0, 1000), rnd.randint(0, 1000)))
            self.hearts.append(nazwa)
            self.add_widget(nazwa)

        if (self.game_event_counter % 600) == 0:
            nazwa = Big_Right_Boost(pos=(rnd.randint(0, 1000), rnd.randint(0, 1000)))
            self.charge_boosts.append(nazwa)
            self.add_widget(nazwa)

        if (self.game_event_counter%300) == 0:
            nazwa = Elephant(pos=(rnd.randint(0, 1000), rnd.randint(0, 1000)))
            self.enemies.append(nazwa)
            self.add_widget(nazwa)



        #moze by tak wprowadzic caly level ze
        if self.game_event_counter >= 1000 and  self.game_event_counter <= 6000:
            if (self.game_event_counter % 500) == 0 and self.hero.experience >= 200:
                nazwa = L2Tile(pos=(rnd.randint(0, 900), rnd.randint(0, 1000)))
                self.l2tiles.append(nazwa)
                self.add_widget(nazwa)



        self.asc_tiles.update(dt)#updateuje to ruszajace sie tilesy
        for self.asc_tile in self.asc_tiles.children:# iteruje przez liste
            if self.asc_tile.collide_widget(self.hero):#kolizja elementow listy tiki
                self.hero.y = self.asc_tile.asc_tile_1.top#umiesc bohatera na gornej podlodze tile
                self.hero.x += 5  # przesuwa bohatera w prawo
                self.hero.running = True#kaze animacji sie dziac, ale nie dziala
            else:
                self.hero.running = False#

        print(self.game_event_counter)

        for heart in self.hearts:
            if self.hero.collide_widget(heart):
                self.hero.hp += 100#O TYM POMYSL
                heart.opacity =0
                self.hearts.remove(heart)

        for boost in self.charge_boosts:
            if self.hero.collide_widget(boost):
                self.hero.charge_power += boost.boost_amount
                boost.opacity =0
                self.charge_boosts.remove(boost)

        for tile in self.l2tiles:
            if self.hero.collide_widget(tile):
                self.hero.x += 8
                self.hero.running = True  # aktywuje animacje
                self.hero.y = tile.top  # uklada bohatera na gorze tila
                 # przesuwa bohatera

        for weapon in self.bullets:
            for enemy in self.enemies:
                if weapon.collide_widget(enemy):
                    enemy.on_hit(weapon)
                    #self.bullets.remove(weapon)
        #USUWANIE TEGO SPRAJTA POWINNO BYC W JEGO KLASIE
        #for weapon in self.bullets:
            #if weapon.x >= 900:
                #self.bullets.remove(weapon)
                #ZAMIAST USUWAC, PRZESTAJE SIE RUSZAC




               # self.l2tiles.remove(tile) to wastawiasz do instrulkcj warunkowej usuwajacej tile jak przejda za ekran jeski bedzie potrzebne to

        self.hero.monster_touched = False  # wylacza animacje ataku
        for enemy in self.enemies:
            if self.asc_tile.collide_widget(enemy):  # przesuwa treemana przy kolizji z asctilem
                enemy.on_basic_tile_touch()
                enemy.floorcoll = True #powinno aktywowac animacje ruchu potwora? przy kolizji z tilem
            else:
                enemy.floorcoll = False
            if self.tile_1.collide_widget(enemy):  # jesli treeman dotyka tila 1 czyli tego na dole
                enemy.on_basic_tile_touch()  # przesuwa w prawo
            if self.tile_2.collide_widget(enemy):  # jesli treeman dotyka tila 2 czyli tego nagorze
                enemy.on_basic_tile_touch() # przesuwa w lewo
            #OOO ELEPHANT TO MA MIEC INNE OBRAZENIA I W OGOLE!
            if self.hero.collide_widget(enemy):  # jesli bohater ma kolizje z treemanem
                enemy.on_hit(self.hero)#TUTAJ ZASZLY ZMIANY, ZOSTALO PRZENIESIONE DO POTWOROW

            enemy.collision = False

            if enemy.collide_widget(self.hero) and enemy.dead == False:  # jesli treeman dotknie hero
                enemy.collision = True  # odpala animacje ataku treemana
                self.hero.hp -= enemy.calc_dmg(self.hero)#TUTAJ ZOSTALY POCZYNIONE ZMIANY, ZOSTALO PRZENIESIONE DO POTWORA
                # #odcina hp u hero

                 # wylacza animacje ataku i treemana
            # if enemy.treeman_dead == False:


            # MONSTER DEATH(MOZE TUTAJ DROP?)
            if enemy.expdrop == True:
                self.hero.experience += 100
                self.enemies.remove(enemy)
                enemy.expdrop = False











        # z jakiegos powodu nie moge w tym iteratorze animowac.


        #MONSTER COLLISIONS WITH OBJECTS



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

        #MONSTER COLLISION WITH HERO



        #kolizje warunkujace koniec gry przy dotknieciu prawej oraz lewej czesci ekranu
        if self.hero.collide_widget(self.left_death):
            self.game_over = True

        if self.hero.collide_widget(self.right_death):
            self.game_over = True
        #else
        #print(self.hero.experience)
        #print(self.hero.hp)
        if self.hero.hp <= 0:
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