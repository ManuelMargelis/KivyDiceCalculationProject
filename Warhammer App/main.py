
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="Name: "))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="last name: "))
        self.lastname = TextInput(multiline=False)
        self.inside.add_widget(self.lastname)

        self.inside.add_widget(Label(text="Age: "))
        self.Age = TextInput(multiline=False)
        self.inside.add_widget(self.Age)

        self.inside.add_widget(Label(text="Bofa: "))
        self.Bofa = TextInput(multiline=False)
        self.inside.add_widget(self.Bofa)

        self.add_widget(self.inside)

        self.submit = Button(text = "Run", font_size=40)
        self.submit.bind(on_press =self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        name = self.name.text
        last = self.lastname.text
        age = self.Age.text
        bofa = self.Bofa.text
        print("pressed!")
        #the next stuff will clear everything from the text boxes
        #self.name.text = ""
        #self.lastname.text = ""
        #self.Age.text = ""
        #self.Bofa.text = ""


class PongGame(Widget):
    pass


class PongApp(App):
    def build(self):
        return MyGrid()


PongApp().run()