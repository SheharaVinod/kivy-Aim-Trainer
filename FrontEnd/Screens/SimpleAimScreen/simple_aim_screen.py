from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder
from kivy.properties import NumericProperty,StringProperty

Builder.load_string("""
<SimpleAimScreen>:
    MDBoxLayout:
        orientation:"vertical"
        
        TitleBar:
        ShootingAria:
        ScoreBoard:
            id:score_bord_counter
            font_size_for_all:28
            bold_for_all:True
            kill_count:root.kill_count
            friendly_fire_count:root.friendly_fire_count
            kf_ratio_count:root.kf_ratio_count
    

""")


class SimpleAimScreen(MDScreen):
    kill_count = NumericProperty(0)
    friendly_fire_count = NumericProperty(0)
    kf_ratio_count = NumericProperty(0)


