from kivy.lang.builder import Builder
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivy.uix.button import ButtonBehavior
from kivy.properties import StringProperty, NumericProperty

Builder.load_string("""
<AimButton>:
    size_hint:None,None
    size: root.b_radius,root.b_radius
    MDAnchorLayout:
        size_hint:None,None
        size:[root.b_radius+root.b_radius*1.5,root.b_radius+root.b_radius*1.5]
        Image:
            source:root.aim_img_source
            center_x:self.parent.center_x
            center_y:self.parent.center_y
        
""")


class AimButton(ButtonBehavior,MDAnchorLayout):
    aim_img_source = StringProperty("assert/image/EnemyAim.png")
    b_radius = NumericProperty(20)
    def __init__(self,**kwargs):
        super(AimButton, self).__init__(**kwargs)




