from kivy.lang.builder import Builder
from FrontEnd.Components.RandomLayout.random_layout import RandomLayout
from FrontEnd.Components.AimButton.aim_button import AimButton

Builder.load_string("""
<ShootingAria>:
    

""")

class ShootingAria(RandomLayout):



    def on_kv_post(self, base_widget):
        self.add_enemies()


    def add_enemies(self,count=1):
        self.target_button = AimButton(on_press=(lambda *x: self.kill_the_enemy()))
        self.add_widget(self.target_button)

    def kill_the_enemy(self):
        self.remove_widget(self.target_button)
        self.add_enemies()
        self.parent.parent.ids.score_bord_counter.kill_count+=1
