from sprite import *
from kivy.clock import Clock

class Treeman(Sprite):
    def __init__(self, pos):  # przywoluje w konstruktorze pozycje
        super(Treeman, self).__init__(source='atlas://img/treeman_anim/tree-attack2', pos=pos)
        #ANIMACJE - LISTY JSONOWE ANIMACJE
        self.attack_animation = ['atlas://img/treeman_anim/tree-attack1', 'atlas://img/treeman_anim/tree-attack2',
                                 'atlas://img/treeman_anim/tree-attack3', 'atlas://img/treeman_anim/tree-attack4',
                                 'atlas://img/treeman_anim/tree-attack5', 'atlas://img/treeman_anim/tree-attack6',
                                 'atlas://img/treeman_anim/tree-attack7', 'atlas://img/treeman_anim/tree-attack8',
                                 'atlas://img/treeman_anim/tree-attack9', 'atlas://img/treeman_anim/tree-attack10']
        self.death_animation = ['atlas://img/treeman_anim/tree-death1', 'atlas://img/treeman_anim/tree-death2',
                                'atlas://img/treeman_anim/tree-death3', 'atlas://img/treeman_anim/tree-death4']
        self.run_animation = ['atlas://img/treeman_anim/tree-run1', 'atlas://img/treeman_anim/tree-run2',
                              'atlas://img/treeman_anim/tree-run3', 'atlas://img/treeman_anim/tree-run4']
        self.collision = False  # bool odpowiadajacy za odpalenie animacji ataku przy kolizji z bohaterem
        self.floorcoll = False  # bool odpowiadajacy z a odpolenie animacji ruchu przy kolizji z podloga
        self.dead = False  # bool odpowiadajacy za odpalenie animacji smierci po smierci treemana
        self.expdrop = False  # bool odpowiadajacy za dawanie expa bohaterowi jak treeman hp  = 0
        self.monster_touch = 0  # liczy dotkniecie potwora
        #self.y = 10  # nadaje losowa pozycje y treemana
        self.y_border_touched = False #bool obslugujacy dolna i gorna granice
        self.x_border_touched = False #bool obslugujacy prawa i lewa granice
        self.hp = 100
        self.sila = 2
        #Clock.schedule_interval(self.update, .0 / 60.0)

    def update(self):  # apdejt klasy

        # tutaj wpisujesz ify lub elify do anumacji ruchu? ktora musialaby sie poprostu moze tutaj zmieniac?
        if self.collision:  # and self.velocity_y < -5: #jesli -kolizja z treemanem
            # self.touch_duration += 1# animacja
            self.monster_touch += 2  # dodaje +2 do
            self.source = self.attack_animation[
                min(len(self.attack_animation) - 1, self.monster_touch // 10)]  # odtwarza animacje ataku
            # elif self.treeman_floorcoll:
            self.monster_touch += 2  # dodaje +2 do
            # self.source = self.run_animation[min(len(self.run_animation) - 1, self.monster_touch // 3)]
        else:
            self.source = self.run_animation[min(len(self.run_animation) - 1, self.monster_touch // 10)]
            self.monster_touch = 0  # resetuje dotyk
        if self.hp <= 20:
            self.source = self.death_animation[min(len(self.death_animation) - 1, self.monster_touch // 10)]

        if self.hp == 0:
            self.dead = True
            self.expdrop = True
            self.opacity = 0

        if self.dead == True:
            self.source = self.death_animation[min(len(self.death_animation) - 1, self.monster_touch // 10)]

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




class Elephant(Sprite):
    def __init__(self, pos):  # przywoluje w konstruktorze pozycje
        super(Elephant, self).__init__(source='atlas://img/traba_anim/eleh-attack1', pos=pos)
        self.attack_animation = ['atlas://img/traba_anim/eleh-attack1', 'atlas://img/traba_anim/eleh-attack2',
                                 'atlas://img/traba_anim/eleh-attack3', 'atlas://img/traba_anim/eleh-attack4',
                                 'atlas://img/traba_anim/eleh-attack5', 'atlas://img/traba_anim/eleh-attack6',
                                 'atlas://img/traba_anim/eleh-attack7', 'atlas://img/traba_anim/eleh-attack8',
                                 'atlas://img/traba_anim/eleh-attack9']
        self.death_animation = ['atlas://img/traba_anim/eleh-death1', 'atlas://img/traba_anim/eleh-death2',
                                'atlas://img/traba_anim/eleh-death3', 'atlas://img/traba_anim/eleh-death4',
                                'atlas://img/traba_anim/eleh-death5']
        self.run_animation = ['atlas://img/traba_anim/eleh-run1', 'atlas://img/traba_anim/eleh-run2',
                              'atlas://img/traba_anim/eleh-run3', 'atlas://img/traba_anim/eleh-run4',
                              'atlas://img/traba_anim/eleh-run5','atlas://img/traba_anim/eleh-run6'
                              ,'atlas://img/traba_anim/eleh-run7','atlas://img/traba_anim/eleh-run8']
        # tutaj wpisujesz run_animation , death_animation albo tree_death cos takiego czyli animacje smierci
        # oraz ruchu
        #self.x = 399  # pozycja x treemana
        self.collision = False  # bool odpowiadajacy za odpalenie animacji ataku przy kolizji z bohaterem
        self.floorcoll = False  # bool odpowiadajacy z a odpolenie animacji ruchu przy kolizji z podloga
        self.dead = False  # bool odpowiadajacy za odpalenie animacji smierci po smierci treemana
        self.expdrop = False  # bool odpowiadajacy za dawanie expa bohaterowi jak treeman hp  = 0
        self.monster_touch = 0  # liczy dotkniecie potwora
        #self.y = 10  # nadaje losowa pozycje y treemana
        self.y_border_touched = False #bool obslugujacy dolna i gorna granice
        self.x_border_touched = False #bool obslugujacy prawa i lewa granice
        self.hp = 100
        self.sila = 1
        #Clock.schedule_interval(self.update, .0 / 60.0)

    def update(self):  # apdejt klasy

        # tutaj wpisujesz ify lub elify do anumacji ruchu? ktora musialaby sie poprostu moze tutaj zmieniac?
        if self.collision:  # and self.velocity_y < -5: #jesli -kolizja z treemanem
            # self.touch_duration += 1# animacja
            self.monster_touch += 2  # dodaje +2 do
            self.source = self.attack_animation[
                min(len(self.attack_animation) - 1, self.monster_touch // 10)]  # odtwarza animacje ataku
            # elif self.treeman_floorcoll:
            self.monster_touch += 2  # dodaje +2 do
            # self.source = self.run_animation[min(len(self.run_animation) - 1, self.monster_touch // 3)]
        else:
            self.source = self.run_animation[min(len(self.run_animation) - 1, self.monster_touch // 10)]
            self.monster_touch = 0  # resetuje dotyk
        if self.hp <= 10:
            self.source = self.death_animation[min(len(self.death_animation) - 1, self.monster_touch // 10)]


        if self.hp == 0:
            self.dead = True
            self.expdrop = True
            self.opacity = 0
            #self.opacity = 0#sprawia ze znika


        if self.dead == True:
            self.source = self.death_animation[min(len(self.death_animation) - 1, self.monster_touch // 10)]
              # sprawia ze znika

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




