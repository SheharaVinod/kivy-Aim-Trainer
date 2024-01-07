from kivy.lang.builder import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import NumericProperty ,BooleanProperty

Builder.load_string("""
<ScoreBoard>:
    size_hint_y:None
    height:80
    md_bg_color:[0.81,0,0.4,1]
    
    MDBoxLayout:
    MDBoxLayout:
        id:Enemy_kills
        size_hint_x:None
        width:200
        MDLabel:
            text:"Kills :"            
            halign:"center"
            font_size:f"{root.font_size_for_all}sp"
            size_hint_x:None
            width:120
            color:[1,1,1,1]
            bold:root.bold_for_all
        MDLabel:
            text:str(root.kill_count)
            font_size:f"{root.font_size_for_all}sp"
            color:[1,1,1,1]
            halign:"center"
            bold:root.bold_for_all
    MDBoxLayout:
        size_hint_x:None
        width:20
    
    MDBoxLayout:
        id:Friendly_fire
        size_hint_x:None
        width:340
        MDLabel:
            text:"Friendly Fires :"
            size_hint_x:None
            width:240
            halign:"center"
            font_size:f"{root.font_size_for_all}sp"
            color:[1,1,1,1]
            bold:root.bold_for_all
        MDLabel:
            text:str(root.friendly_fire_count)
            font_size:f"{root.font_size_for_all}sp"
            color:[1,1,1,1]
            halign:"center"
            bold:root.bold_for_all

    MDBoxLayout:
        size_hint_x:None
        width:20
        
    MDBoxLayout:
        id:Enemy_Friend_Ratio
        size_hint_x:None
        width:200
        MDLabel:
            text:"E/F Ratio :"
            size_hint_x:None
            width:140
            halign:"center"
            font_size:f"{root.font_size_for_all}sp"
            color:[1,1,1,1]
            bold:root.bold_for_all
        MDLabel:
            text:str(root.kf_ratio_count)
            font_size:f"{root.font_size_for_all}sp"
            color:[1,1,1,1]
            halign:"center"
            bold:root.bold_for_all
    MDBoxLayout:
    
        
""")

class ScoreBoard(MDBoxLayout):
    font_size_for_all = NumericProperty(24)
    bold_for_all = BooleanProperty(False)

    kill_count = NumericProperty(0)
    friendly_fire_count = NumericProperty(0)
    kf_ratio_count = NumericProperty(0)
