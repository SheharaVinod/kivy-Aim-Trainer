from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder

Builder.load_string("""
<SimpleAimScreen>:
    MDBoxLayout:
        orientation:"vertical"
        
        TitleBar:
        ShootingAria:
        ScoreBoard:
    

""")


class SimpleAimScreen(MDScreen):
    pass
