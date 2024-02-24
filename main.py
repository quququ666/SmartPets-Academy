import kivy
from kivy.app import App, runTouchApp
from kivymd.app import MDApp
from kivy.lang.builder import Builder, BuilderBase, BuilderException 
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.scrollview import ScrollView 
from kivymd.uix.scrollview import MDScrollView
from kivy.uix.label import Label
from kivy.core.window import Window 
from kivy.core.text import LabelBase 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget 

#Screen set up
Window.size = (400, 530)
sm = ScreenManager()

#Font Registration
LabelBase.register(name='LoRes', fn_regular='C:\Users\quent\Downloads\HackTJ\Fonts\LoRes9OTWide-Bold.ttf')
LabelBase.register(name='LoResReg', fn_regular='C:\Users\quent\Downloads\HackTJ\Fonts\LoRes9OTWide-Regular.ttf')
LabelBase.register(name='LoResBold', fn_regular='C:\Users\quent\Downloads\HackTJ\Fonts\LoRes15OT-Bold.ttf')

#Builder string
kv = Builder.load_string(
"""
<Opening>:
    ScrollView:
        Label:
            text: "Hello!"
""")

#Build Screens
class Opening(Screen):
    pass 

class childApp(App):
    def build(self):
        sm.add_widget(Opening(name='opening'))

        return sm
    
#Run The Application
if __name__ == '__main__':
    childApp().run()