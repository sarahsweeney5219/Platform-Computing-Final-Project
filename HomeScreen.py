from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
Window.clearcolor = (1, 1, 1, 1)
#https://www.reddit.com/r/kivy/comments/aam90x/why_a_kv_file/

def switch_to_signup():
    from main import sm

class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("HomePage.kv")


class LoginPage(App):
    kv = Builder.load_file("Homepage.kv")
    def build(self):
        return kv
    
if __name__ == "__main__":
    LoginPage().run()