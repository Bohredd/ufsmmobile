from kivy.clock import Clock, mainthread
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivy.uix.image import AsyncImage
from kivy.uix.scatter import Scatter
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


screen = ScreenManager()

class TelaInicio(Screen):
    pass

class TelaPesquisa(Screen):
    dialog = None
    def checkbox_click_foto(self,instance,value): 
        foto_value = value
        return foto_value

    def checkbox_click_mapa(self,instance,value):
        mapa_value = value
        return mapa_value

    def checkbox_click_caminho(self,instance,value):
        caminho_value = value
        return caminho_value

    def escolhidos(self,foto,mapa,caminho):
        if foto == True:
            print("foto")   
        if caminho == True:
            print("caminho")
        if mapa == True:
            print("mapa")

    def close_dialog(self,obj):
        self.dialog.dismiss()

    def testar_nome_predio(self):
        text = self.ids.nome_predio.text 
        if(text == ''):
            if not self.dialog:
                self.dialog = MDDialog(
                    text="Insira corretamente o campo!",
                    buttons=[
                        MDFlatButton(
                            text="Ok!",
                            theme_text_color="Custom",
                            on_release = self.close_dialog
                        )
                    ],
                )
            self.dialog.open()
        else:
            MDApp.get_running_app().root.current = 'predio'
            print(f"Nome do predio = {self.ids.nome_predio.text}")
            self.ids.nome_predio.text = ''

class MostrandoPredio(Screen):
    pass
screen.add_widget(TelaInicio(name='incio'))
screen.add_widget(TelaPesquisa(name='home'))
screen.add_widget(MostrandoPredio(name='predio'))

class UFSMAPP(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        kv = Builder.load_file("main.kv")
        screen = kv
        return screen

    def on_start(self):
        self.fps_monitor_start()


if __name__ == "__main__":
    UFSMAPP().run()