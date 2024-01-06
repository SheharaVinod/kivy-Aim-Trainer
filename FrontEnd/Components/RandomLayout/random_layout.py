from kivy.lang.builder import Builder
from kivymd.uix.relativelayout import MDRelativeLayout
import random

Builder.load_string("""
<RandomLayout>:


""")

class RandomLayout(MDRelativeLayout):

    def random_pos_generator(self,x,y):
        pos = x,y

