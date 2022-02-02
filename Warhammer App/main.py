import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    numofattacks = ObjectProperty(None)
    email = ObjectProperty(None)
    rerollH = ObjectProperty(None)
    wounding = ObjectProperty(None)
    rerollW = ObjectProperty(None)
    Saves = ObjectProperty(None)
    dmg = ObjectProperty(None)

    def btn(self):
        print(self.numofattacks.text, self.email.text, self.rerollH.text, self.wounding.text, self.rerollW.text, self.saves.text, self.dmg.text)
        attacks = float(self.numofattacks.text)
        hitting = float(self.email.text)
        attackreroll = float(self.rerollH.text)
        wounding = float(self.wounding.text)
        woundreroll = float(self.rerollW.text)
        save = float(self.saves.text)
        damage = float(self.dmg.text)
        runningtotal = abs(7 - hitting)
        runningtotal = runningtotal/6
        runningtotal = runningtotal*attacks
        print(runningtotal)
        if attackreroll == 1:
            i = attacks*(1/6)
            n = abs(7 - hitting)
            n = n/6
            i = i*n
            print(i)
            runningtotal = runningtotal + i
            print(runningtotal)

        if attackreroll == 6:
            misses = hitting - 1
            misses = misses/6
            numattackreroll = misses*attacks
            i = abs(7 - hitting)
            i = i/6
            numattackreroll = numattackreroll*i
            print(numattackreroll)
            runningtotal = runningtotal + numattackreroll
            print(runningtotal)

        i = abs(7 - wounding)
        i = i/6
        runningtotal = runningtotal*i


        if woundreroll == 1:
            n = abs(7 - hitting)
            n = n / 6
            i = attacks*n*(1/6) #number of attacks to hit and have a wound of 1
            m = abs(7 - wounding)
            m = m/6
            resultofrerollingallonesonwounds = i*m
            runningtotal = runningtotal + resultofrerollingallonesonwounds
            #print("running total =")
            #print(runningtotal)

        #if woundreroll == 6:
            #do stuff here

        n = abs(7- save)
        n = n/6
        n = 1-n
        print(n)
        runningtotal = runningtotal*n

        runningtotal = runningtotal*damage

        self.ids.finalanswer.text = str(runningtotal)



        self.numofattacks.text = ""
        self.email.text = ""
        self.rerollH.text = ""
        self.wounding.text = ""
        self.rerollW.text = ""
        self.saves.text = ""
        self.dmg.text = ""




class CalcApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    CalcApp().run()