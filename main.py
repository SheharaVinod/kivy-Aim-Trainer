from kivy.config import Config
Config.set("graphics", "minimum_height", "600")
Config.set("graphics", "minimum_width", "800")
Config.set("kivy", "exit_on_escape", "0")
Config.set("input", "mouse", "mouse,disable_multitouch") # NOQA
from kivymd.app import MDApp  # NOQA
from os.path import exists  # NOQA
from FrontEnd import RootWindow

class KivyAimTrainer(MDApp):
    def __init__(self, **kwargs):
        super(KivyAimTrainer, self).__init__(**kwargs)
        self.title = "Aim Trainer"
        self.icon = "assert/image/Aim.png"

    def build(self):
        return RootWindow()


if __name__ == '__main__':
    MainLoop = KivyAimTrainer()
    is_exists = None
    wanted_files = [
        "assert/image/Aim.png",
        "assert/image/EnemyAim.png",
        "assert/image/FriendAim.png",
        "icon.ico"
    ]
    wanted_file = []
    for every_single_file in wanted_files:
        if not exists(every_single_file):
            is_exists = False
            wanted_file.append(every_single_file)

    if is_exists == False: # NOQA
        print(*tuple(wanted_file))
        raise FileExistsError("These files are missing :")
    else:
        MainLoop.run()
