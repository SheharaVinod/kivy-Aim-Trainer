from kivy.lang.builder import Builder
from kivymd.uix.relativelayout import MDRelativeLayout
import random

Builder.load_string("""
<RandomLayout>:


""")


class RandomLayout(MDRelativeLayout):

    def __init__(self,**kwargs):
        super(RandomLayout, self).__init__(**kwargs)
        fbind = self.fbind
        update = self._trigger_layout
        fbind("on_size",update)

    def _random_pos_generator(self):
        # get random two position
        child_x = random.randint(0, self.width)
        child_y = random.randint(0, self.height)
        return child_x, child_y

    def add_widget(self, widget, *args, **kwargs):
        widget.pos = self._random_pos_generator()
        return super(RandomLayout, self).add_widget(widget)
