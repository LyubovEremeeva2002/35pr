from re import X
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers import HtmlLexer



from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter

class myApp(App):
    def build(self):
        fl=FloatLayout(size=(200, 200))
        fl.add_widget(Button(
            text="1 кнопка",
            font_size=20,
            on_press=self.btn_press,
            background_color=[0,1,0,1],
            background_normal='',
            size_hint=(.15, .10),
            pos=(100, 300)))
        
        fl.add_widget(Button(
            text="2 кнопка",
            font_size=20,
            on_press=self.btn_press,
            background_color=[1,1,0,1],
            background_normal='',
            size_hint=(.15, .10),
            pos=(300, 300)))
        return fl
    x = 1
    y = 1
    def btn_press(self, instance):
        if  instance.text =="1 кнопка":
            instance.text='Я нажата 1'
        if instance.text == "2 кнопка":
            instance.text ='Я нажата 2'

        
if __name__=="__main__":
    myApp().run()
