from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.config import Config
#from kivymd.app import MDApp

Config.set('kivy', 'keyboard_mode', 'systemanddock')

from kivymd.theming import ThemeManager


from pyowm import OWM
# from pyowm.utils import config
# from pyowm.utils import timestamps

owm = OWM('8d83a7e3272b9d4e6eefef7fbb1fdd91')
mgr = owm.weather_manager()

Window.size = (360, 640)

class Container(GridLayout):
    txt_in = ObjectProperty()
    txt_liable = ObjectProperty()

    def weather(self):
        try:
            observation = mgr.weather_at_place(self.txt_in.text)
            w = observation.weather
            temp_now = w.temperature('celsius')['temp']
        except:
            temp_now = 'Не найден'

        if temp_now == 'Не найден':
            self.txt_liable.text = temp_now
        else:
            self.txt_liable.text = \
                str(f'*{self.txt_in.text}*\n'
                    f' в данный\n'
                    f' момент:\n'
                    f' {temp_now} \n'
                    f'градусов')


class MyApp(App):
    theme_cls = ThemeManager()
    title = 'Weather'

    def build(self):
        self.theme_cls.theme_style = "Light"
        return Container()


if __name__ == '__main__':
    MyApp().run()
