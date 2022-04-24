from sprite import *
from kivy.clock import Clock
from random import *
#SMIESZNA SPRAWA, JA TYLE EDYTOWALEM TEST WEAPON, A TO WEAPON DZIALA
class Test_Weapon(Sprite):
    def __init__(self, pos):  # przywoluje w konstruktorze pozycje
        super(Test_Weapon, self).__init__(source='img/sky sword.png')
        self.activated = False
        self.damage = randrange(1, 5)
        self.bullets =[]
        self.shoot = False

        for t in self.bullets:
            self.add_widget(t)

    def update(self):
    # apdejt klasy
        for bullet in self.bullets:
            bullet.update()


    def weapon_equipped(self,owner):
        if owner.experience >= 1000:
            self.activated = True


    def on_touch_down(self, *ignore):#tu jest metoda ktora sprawia ze gdy dotkniemy ekranu
        self.shoot = True
        self.x += 10
'''
jakich modulow potrzebujemy? potrzebujemy modulu do 
#modul odpowiadajacy za aktywacje broni do zastosowania przy kolizji z bohaterem,
modul odpowiadajacy za obliczenie obrazen przy kolizji z potworem.
musze pamietac ze wzglem potworw jakby sprawa jest chyba rozwiazana? gdy masz juz taki modul w potworze, wystarczy ze dodam w broni takie zmienne jak bohaterze,
co oznacza ze NP CHARGE POWER BRONI ORAZ SILA KURWA ZAPOMNIALEM
aa ze charge power broni byloby takie jak np ten += x ktory ja przesuwa! 

ACTIVE
dodam wiec sile i charge power do broni, skoro kalkulacja 


DALEKO IDACY POMYSL
i moze by ja tak rzucal jak w castlewanii? dodac jej velocity i grawitacje, byloby smiesznie 

NAPISAC JAK SOBIE WYOBRAZAM ZE MIALABY DZIALAC BRON

NAPISAC JAK WIEM JAK DZIALA MONSTER CLASS MOZE NAWET CALOSC - TUTAJ!

tak wiec deklaruje klase np treemana w pliku monsters, 
robie inita i supera, w superze wpisuje nazwe klasy i w pozycji source wrzcam podstawowy obrazek potworka, ktory w wtej sytuacji jest atlasem.
nastepnie w inicie wypisuje listy zajmujace sie animacja ataku, smierci i biegu(ktory nie dziala)
pare booli odpowadajacych za aktywacja animacji przy kolizji z podloga 
bool odpowiadajacy za smierc
boole odpowiadajace za dotykanie borderow, ktore w updacie sa wypisane do zmiany pozycji y potwora.
ilosc zycia oraz ilosc sily.

po inicie mamy:
modul odpowiadajacy za aktywacje animacji, przesuniecie potwora oraz obliczanie obrazen, do zastosowania przy kolizji z bohaterem.
GDZIE JEST AKTYWOWANY?

modul odpowiadajacy za kalkulacje obrazen uzywany przy kolizji prawdopodobnie
GDZIE JEST AKTYWOWANY?

modul odpowiadajacy za przesuniecie potwora w prawo, aktywowany przy kolizji z tilem prawdopodobnie 

nastepne po modulach mamy update klasy, w ktorym 
mamy instrukcje warunkowe dotyczace kolizji, aktywuje animacje ataku, i w elsie animacje biegu ktora nei dziala.

instrukcje warunkowa przy hp mniejszym niz dziesiec aktywajacy animacje smierci  , i drugiego od hp zero warunkujaca znikniecie itp
poza tym granice

nastepnie w game.py - 
w inicie w game tworze liste enemies
czylistworzylbym liste weapons czy bullets
potem masz forloopa appendujacego widzety do powierzchni., ale dalej w inicie
        for w in self.enemies:#forloop ktory appenduje widzety ktore zostaly dodane w inicie A TO ITERUJE PRZEZ NIA I WRZUCA JE NA EKRAN
            self.add_widget(w)
        
        w updace klasy game masz :
        
        for heart in self.hearts:
            heart.update()
        czyli forloopa iterujacego przez liste i updateuje 
        
i potem w instrukcji warunkowej


        if (self.game_event_counter%200) == 0: wgledem czasu 
            nazwa = Treeman(pos=(rnd.randint(0, 1000), rnd.randint(0, 1000)))
            self.enemies.append(nazwa)
            self.add_widget(nazwa)
            
            czyli moglbym zrobic instrukcje warunkowa 
        if self.hero.experience >= 1000:
            nazwa = Weapon(pos=(self.hero.x + 5,self.hero.y + 0.3))
            self.bullets.append(nazwa)
            self.add_widget(nazwa)
            
            
    potem przechodzimy do instrukcji warunkowych zwiazanych z kolizjami.
        czyli kolizje z bohaterem oraz
            for weapon in self.bullets:
                if self.hero.collide_widget(weapon):
                    weapon.opacity =0
                    self.bullets.remove(weapon)
                if .collide_widget(weapon):
                
        kolizje broni z enemy robimy w forloopie enemy.
                    


wklasie broni chcialbym 
inita i supera, w inicie wpisuje nazwe klasy i w pozycji source chcialbym wrzucic podstawowy obraz broni??, ktory moglby byc atlasem, jakbym polaczyl wszystkie w bronie spritesheeta 
i zrobil listy broni, albo nawet ZROBIC ANIMACJE ATAKU, i zrobic z nich listy animacji, to by bylo chyba w chuj najprostsze, w kazdym razie namy source podstwowej broni,
i potem moze bym zrobil m




'''

class Weapon(Sprite):
    def __init__(self, pos):  # przywoluje w konstruktorze pozycje
        super(Weapon, self).__init__(source='img/csharp bullet.png', pos=pos)
        self.activated = False
        self.damage = randrange(10, 15)
        self.shoot = False
        self.sila = 12
        self.charge_power = 3


    #def weapon_equipped(self, owner):
        #if owner.experience >= 100:
           #self.activated = True

    #def on_touch_down(self, *ignore):  # tu jest metoda ktora sprawia ze gdy dotkniemy ekranu
       #if self.shoot == True:
        #self.x + 10

    def update(self):  # apdejt klasy
        self.x += 10
        if self.x >= 990:
            self.opacity = 0
            self.source =''


        # tutaj wpisujesz ify lub elify do anumacji ruchu? ktora musialaby sie poprostu moze tutaj zmieniac?




