from sprite import *

class Hero(Sprite):
    def __init__(self, pos): #przywoluje w konstruktorze pozycje
        super(Hero, self).__init__(source='atlas://img/hero_anim/wing-run1', pos=pos)#superuje atlas i pozycje- tutaj chyba poczatkowo przypisujemy obrazek
        self.velocity_y = 0 #zmeinna do skakania
        self.gravity = -.3 #grawitacja ktora bedzie wplywac na bohatera BASE -.3
        self.attack_animation = ['atlas://img/hero_anim/wing-attack1', 'atlas://img/hero_anim/wing-attack2',
                                 'atlas://img/hero_anim/wing-attack3', 'atlas://img/hero_anim/wing-attack4']
        self.run_animation = ['atlas://img/hero_anim/wing-run1', 'atlas://img/hero_anim/wing-run2',
                              'atlas://img/hero_anim/wing-run3', 'atlas://img/hero_anim/wing-run4',
                              'atlas://img/hero_anim/wing-run5']
        self.touch_duration = 0 #touch duration dlugosc przycisniecia TIMER ANIMACJI
        self.attack_duration = 0
        self.running = False  #bool aktywuujacy animacjie bieguPRZY KOLIZJI Z czyms- czyli z TILEM
        self.experience = 0 #podstawowa ilosc doswiadczenia.
        self.experience_level = int(self.experience//100)#proba stworzenia czegos w stylu poziomu doswiadczenia.
        self.monster_touched = False #bool aktywujacy animacje ataku przy kolizji z potworem POWINNA NAZYWAC SIE HERO TOUCHING MONSTER
        self.hp = 130 #podstawowa ilosc zycie bohatera
        self.sila = 10 #podstawowa sila bohatera - narazie ma przelozenie tylko na obrazenia przy walce.
        self.charge_power = 1#charge power- w malutki sposob wplywa na to jak daleko bohater przesuwa sie do przodu przy skoku, dodaje cosik do kalkulowania obrazen

    def update(self):
        self.velocity_y += self.gravity #przyrownuje do siebie velocity z grawitacja
        self.velocity_y = max(self.velocity_y, -10)#robi cos mat z ta velocity, moze pozmieniac fajnie da sie?
        self.y += self.velocity_y #zmienia y czyli pozycje w poziomie bohatera na podstawie grawitacji
        if self.velocity_y < -3:#instrukcje warunkowe warunkujace pojedyncze animacje (zmiany obrazka poprostu)
            self.source = 'atlas://img/hero_anim/wing-run3'
        elif self.velocity_y < 0:
            self.source = 'atlas://img/hero_anim/wing-attack1'

        #INSTRUKCJA WARUNKOWA AKTYWUJACA ANIMACJE BIEGU, ITERUJAC PRZEZ NIA. (NIE DZIALA W KONTEKCIE LIST OBIEKTOW - A ATAK DZIALA W KOTNEKSCIE POTWOROW- COS JEST NA RZECZY
        if self.running:
            self.touch_duration += 1
            self.source = self.run_animation[min(len(self.run_animation) - 1, self.touch_duration // 30)]
        else:
            self.touch_duration = 0
        # INSTRUKCJA WARUNKOWA AKTYWUJACA ANIMACJE ATAKU, ITERUJAC PRZEZ NIA.\
        if self.monster_touched:
            self.attack_duration += 2
            self.source = self.attack_animation[min(len(self.attack_animation) - 1, self.attack_duration // 30)]
        else:
            self.attack_duration = 0

    def on_touch_down(self, *ignore):#tu jest metoda ktora sprawia ze gdy dotkniemy ekranu
        self.velocity_y = 5.5#5.5#to velocity_y sie zwieksza i skaczemy
        self.x += self.charge_power/100 #tutaj kalkuluje jak daleko przesuwa ziomala- w chuj niedaleko, malutkie ilosci.
        self.source =  'atlas://img/hero_anim/wing-attack4'#tu tez jest warunkowana pojdydncza animacja

