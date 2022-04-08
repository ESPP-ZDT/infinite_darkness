from kivy.uix.image import Image

class Sprite(Image):#subklasa image ktora resizuje image- tak zeby miala swoj rozmiar
    def __init__(self,**kwargs):
        super(Sprite,self).__init__(**kwargs)
        self.size = self.texture_size