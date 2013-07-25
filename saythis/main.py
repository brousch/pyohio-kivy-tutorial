import kivy
kivy.require('1.7.0')

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout

from components.initialize import InitializePlatform
from components.ttsspeak import TtsSpeak


class SayThis(FloatLayout):
    saywhat_text = ObjectProperty(None)

    def say_something(self, text):
        TtsSpeak(text).speak()

    def clear(self):
        self.saywhat_text.text = ""
        self.saywhat_text.focus = True

class SayThisApp(App):
    def build(self):
        InitializePlatform()
        return SayThis()
    

if __name__ == '__main__':
    SayThisApp().run()
