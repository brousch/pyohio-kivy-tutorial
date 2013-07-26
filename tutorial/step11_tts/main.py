import kivy
kivy.require('1.7.1')

import subprocess

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout


class SayThis(BoxLayout):
    saywhat_text = ObjectProperty(None)
    
    def say_something(self, text):
        subprocess.call(["espeak", text])
    
    def clear(self):
        self.saywhat_text.text = ""
        self.saywhat_text.focus = True

class SayThisApp(App):
    def build(self):
        return SayThis()
    

if __name__ == '__main__':
    SayThisApp().run()
