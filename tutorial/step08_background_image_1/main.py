import kivy
kivy.require('1.7.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class SayThis(BoxLayout):
    pass

class SayThisApp(App):
    def build(self):
        return SayThis()
    

if __name__ == '__main__':
    SayThisApp().run()
