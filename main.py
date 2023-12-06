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

class BoxLayoutExample(BoxLayout):
     pass

class WidgetsExample(GridLayout): 
     my_text = StringProperty("Hello!")   
     def on_button_click(self):
          print("button clicked")
          self.my_text = "You clicked"

class MainApp(MDApp):

    def build(self):
        layout = MDBoxLayout(orientation='vertical')
        layout.add_widget(Button(
            text="Color Detection",
            pos_hint={'center_x':.5, 'center_y':.5},
            size_hint=(.2,.2)
        ))
        self.image = Image()
        layout.add_widget(self.image)
        layout.add_widget(MDRaisedButton(
            text="Yellow Detection Apps",
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

        colorLower = (29,86,6)
        colorUpper = (64, 255, 255)

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
    MainApp().run()






    
