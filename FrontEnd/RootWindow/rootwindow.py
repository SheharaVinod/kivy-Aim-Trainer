from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang.builder import Builder

Builder.load_string("""
<RootWindow>:
    orientation:"vertical"
    SimpleAimScreen:
    
""")

class RootWindow(MDBoxLayout):
    pass
