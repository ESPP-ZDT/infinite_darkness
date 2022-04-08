from sprite import *

class Hero(Sprite):
    def __init__(self, pos): #przywoluje w konstruktorze pozycje
        super(Hero, self).__init__(source='atlas://img/hero_anim/wing-run1', pos=pos)#superuje atlas i pozycje- tutaj chyba poczatkowo przypisujemy obrazek
        self.velocity_y = 0 #zmeinna do skakania
        self.gravity = -.3 #grawitacja ktora bedzie wplywac na bohatera
        self.attack_animation = ['atlas://img/hero_anim/wing-attack1', 'atlas://img/hero_anim/wing-attack2',
                                 'atlas://img/hero_anim/wing-attack3', 'atlas://img/hero_anim/wing-attack4']
        self.run_animation = ['atlas://img/hero_anim/wing-run1', 'atlas://img/hero_anim/wing-run2',
                              'atlas://img/hero_anim/wing-run3', 'atlas://img/hero_anim/wing-run4',
                              'atlas://img/hero_anim/wing-run5']
        self.touch_duration = 0 #touch duration dlugosc przycisniecia
        self.attack_duration = 0
        self.running = False  #bool aktywuujacy animacjie biegu
        self.experience = 0
        self.experience_level = int(self.experience//100)
        self.monster_touched = False #bool aktywujacy animacje ataku
        self.hero_hp = 130

    def update(self):

        self.velocity_y += self.gravity #przyrownuje do siebie velocity z grawitacja
        self.velocity_y = max(self.velocity_y, -10)#robi cos mat z ta velocity, moze pozmieniac fajnie da sie?
        self.y += self.velocity_y #zmienia y czyli pozycje w poziomie bohatera na podstawie grawitacji
        if self.velocity_y < -3:#to sa ify
            self.source = 'atlas://img/hero_anim/wing-run3'#warunkujace pojedyncze animacje
        elif self.velocity_y < 0:
            self.source = 'atlas://img/hero_anim/wing-attack1'


        if self.running: #and self.velocity_y < -5:
            #self.touch_duration += 1# animacja
            self.touch_duration += 1
            self.source = self.run_animation[min(len(self.run_animation) - 1, self.touch_duration // 30)]
        else:
            self.touch_duration = 0

        if self.monster_touched:
            self.attack_duration += 1
            self.source = self.attack_animation[min(len(self.attack_animation) - 1, self.attack_duration // 30)]
        else:
            self.attack_duration = 0

    def on_touch_down(self, *ignore):#tu jest metoda ktora sprawia ze gdy dotkniemy ekranu
        self.velocity_y = 5.5#to velocity_y sie zwieksza i skaczemy
        self.x += 3
        self.source =  'atlas://img/hero_anim/wing-attack4'#tu tez jest warunkowana pojdydncza animacja
