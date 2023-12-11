# Fitness App Main Code
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from HomeScreen import LoginPage
from kivy.properties import BooleanProperty


class WindowManager(ScreenManager):  # creating a class that deals with screen management
    pass


sm = WindowManager()  # setting a variable to the window manager class

screens = [LoginPage(name="Login_Page")]  # setting an array of lists
for screen in screens:  # going through all of the screens
    sm.add_widget(screen)  # adding the screen widget to each

sm.current = "Login_Page"  # setting current window to login


class ColorDetectApp(App):  # the class that runs the app
    def build(self):
        App.title = "Color Detecting App"  # setting the app title
        return sm  # running the app by returning the current window


if __name__ == '__main__':  # The value of __name__ attribute is set to “__main__” when module is run as main program
    ColorDetectApp = ColorDetectApp()
    ColorDetectApp.run()