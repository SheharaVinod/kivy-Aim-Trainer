from kivy.lang.builder import Builder
from kivymd.uix.boxlayout import MDBoxLayout

Builder.load_string("""
<ScoreBoard>:
    size_hint_y:None
    height:80
    md_bg_color:[0.81,0,0.4,1]

""")

class ScoreBoard(MDBoxLayout):
    pass
