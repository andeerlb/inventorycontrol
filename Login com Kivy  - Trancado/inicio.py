#coding: utf-8

__author__ = "Anderson Babinski"
__copyright__ = "Copyright 2017, Control of Stock"
__email__ = "andeerlb@gmail.com"
__status__ = "Production"

import kivy
kivy.require('1.9.1')

#------ Importações da biblioteca Kivy ----------------------#
from kivy.app import App
from kivy.core.window import Window
#------ Importações da biblioteca Kivy FIM ------------------#

#------ DEFININDO A COR DE FUNDO DO LAYOUT ------------------#
from kivy.utils import get_color_from_hex
Window.clearcolor = get_color_from_hex("#BEBEBE")
#------ DEFININDO A COR DE FUNDO DO LAYOUT FIM --------------#

#------ Importações do módulo CONTROLE DE ESTOQUE -----------#
from menu_estoque import *
#------ Importações do módulo CONTROLE DE ESTOQUE  FIM ------#

class LoginApp(App):
    def build(self):
        pass

    def login(self):
        usuario = self.root.ids.usuario.text
        senha = self.root.ids.senha.text

        # Regras para acesso
        if usuario == 'admin' and senha == 'admin':
            # se usuario e senha iguais a admin, executar modulo controle de estoque
            # se não enviar mensagem na interface gráfica que não constam no banco de dados
            pass

if __name__ == '__main__':
    LoginApp().run()
