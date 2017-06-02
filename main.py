from kivy.app import App
from kivy.uix.label import Label
from shabbos1 import time
class MyApp(App):
	def build(self):
		return Label(text=time())

if __name__ == '__main__':
    MyApp().run()