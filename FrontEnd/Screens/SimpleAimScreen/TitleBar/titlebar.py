from kivy.lang.builder import Builder
from kivymd.uix.boxlayout import MDBoxLayout

Builder.load_string("""
<TitleBar>:
    size_hint_y:None
    height:110
    MDBoxLayout:
        md_bg_color:[1,0,0,1]
    MDBoxLayout:
        md_bg_color:[0,1,0,1]
    MDBoxLayout:
        md_bg_color:[1,0,1,1]

""")

class TitleBar(MDBoxLayout):
    pass

