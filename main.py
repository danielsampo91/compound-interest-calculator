from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class Calcolo(App):
    def build(self):

        self.window = GridLayout()
        self.window.cols = 1
        Window.size = (360, 640)
        self.window.add_widget(Label(text="Calcola l'interesse giornaliero.", size_hint=(1, 0.4)))
        self.window.add_widget(Label(text="Inserisci investimento iniziale:", size_hint=(1, 0.4)))
        #soldi = self.window.add_widget(TextInput(size_hint=(1, 0.5)))
        #self.soldi = soldi

        self.input_soldi = TextInput(size_hint=(1, 0.5))
        self.window.add_widget(self.input_soldi)


        self.window.add_widget(Label(text="Inserisci percentuale di interesse prevista:", size_hint=(1, 0.4)))
        #percentuale = self.window.add_widget(TextInput(size_hint=(1, 0.5)))
        #self.percentuale = percentuale
        self.percentuale = TextInput(size_hint=(1, 0.5))
        self.window.add_widget(self.percentuale)




        self.window.add_widget(Label(text="Inserisci durata investimento(giorni):", size_hint=(1, 0.4)))

        self.giorni = TextInput(size_hint=(1, 0.5))
        self.window.add_widget(self.giorni)

        self.merda = Button(text="Calcola!", size_hint=(1, 0.5))
        self.merda.bind(on_press=self.press)
        self.window.add_widget(self.merda)




        return self.window




    def press(self, instance):
        soldi = self.input_soldi._get_text()
        soldi = int(soldi)
        percentuale = self.percentuale._get_text()
        percentuale = float(percentuale)
        tasso = percentuale / 100
        tasso = float(tasso)
        giorni = self.giorni._get_text()
        giorni = int(giorni)


        tot = soldi * (1 + tasso) ** giorni



        tot2 = ((soldi / 100) * percentuale) * giorni

        self.window.clear_widgets()
        self.window.add_widget(Label(text= str(tot) +"--" + str(tot2) + "$."))

        fine = ""
        return tot, tot2







Calcolo().run()
