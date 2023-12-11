from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2
#from utils import getlimits
from PIL import Image as img
from kivy.uix.button import Button 
from kivy.uix.gridlayout import GridLayout
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.lang import Builder



class BoxLayoutExample(BoxLayout):
     pass

class WidgetsExample(GridLayout): 
     my_text = StringProperty("Hello!")   
     def on_button_click(self):
          print("button clicked")
          self.my_text = "You clicked"

class ColorApp(MDApp):
    #kv = Builder.load_file("SignUpWindow.kv")
    
    def build(self):
        #def __init__():
        self.colorLower = (29,86,6)
        self.colorUpper = (64, 255, 255)

        def change_color_to_red(instance):
            self.colorLower = (160, 100, 100)
            self.colorUpper = (180, 255, 255)

        def change_color_to_yellow(instance):
            self.colorLower = (29,86,6)
            self.colorUpper = (64, 255, 255)

        def change_color_to_green(instance):
            self.colorLower = (70, 50, 50)
            self.colorUpper = (100, 255, 255)

        layout = MDBoxLayout(orientation='vertical')
        red = Button(
            text="Detect Red",
            #pos_hint={'center_x':.5, 'center_y':.5},
            size_hint=(.2,.2),
        )
        red.bind(on_press=change_color_to_red)

        green = Button(
            text="Detect Green",
            #pos_hint={'center_x':.25, 'center_y':.5},
            size_hint=(.2,.2),
        )
        green.bind(on_press=change_color_to_green)

        yellow = Button(
            text="Detect Yellow",
            #pos_hint={'center_x':.75, 'center_y':.5},
            size_hint=(.2,.2),
        )
        yellow.bind(on_press=change_color_to_yellow)

        layout.add_widget(red)
        layout.add_widget(green)
        layout.add_widget(yellow)    


        self.image = Image()
        layout.add_widget(self.image)
        layout.add_widget(MDRaisedButton(
            text="Color Detection App",
            pos_hint={'center_x':.5, 'center_y':.5},
            size_hint=(None,None)
        ))
        
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.load_video, 1/60)
        return layout
    
    def load_video(self, *args):
        ret, frame = self.capture.read()
        #Frame initialize
        self.image_frame = frame

        #color detection
        blurred = cv2.GaussianBlur(frame, (11,11),0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)


        #ValidgreencolorLower = (50, 100, 100)
        #ValidgreencolorUpper = (70, 255, 255)
        colorLower = self.colorLower
        colorUpper = self.colorUpper
        #ValidRedcolorLower = (160, 100, 100)
        #ValidRedcolorUpper = (180, 255, 255)

        #ValidYellowcolorLower = (29,86,6)
        #ValidYellowcolorUpper = (64, 255, 255)
        mask = cv2.inRange(hsv,colorLower,colorUpper)
        mask = cv2.erode(mask, None, iterations=3)
        mask = cv2.dilate(mask, None, iterations=3)

        mask_ = img.fromarray(mask)
        bbox = mask_.getbbox()

        if bbox is not None:
            x1,y1, x2, y2 = bbox
            frame = cv2.rectangle(frame, (x1,y1), (x2, y2), (0,255,0), 5)

        buffer = cv2.flip(frame,0).tostring()
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        self.image.texture = texture

        
       
if __name__ == '__main__':
    ColorApp().run()






    
