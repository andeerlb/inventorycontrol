#coding: utf-8

__author__ = "Anderson Babinski"
__copyright__ = "Copyright 2017, Control of Stock"
__email__ = "andeerlb@gmail.com"
__status__ = "Production"

# Importações

from tkinter import *
from tkinter import ttk
from win32api import GetSystemMetrics as Resolucao

#--------- importação do modulo controle de estoque -------#
#--------- importação do modulo controle de estoque -------#

# Variaveis globais
cor_de_fundo_geral = '#3CB371'

class Entrar:
    def __init__(self, myParent):
        self.containerLogin = Frame(myParent)

        # Cor de fundo do cainter
        self.containerLogin.configure(bg=cor_de_fundo_geral)

        # Centraliza o Container no centro da tela
        self.containerLogin.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Labels
        self.lb_usuario = Label(self.containerLogin, text="Usuário:", background=cor_de_fundo_geral)
        self.lb_senha = Label(self.containerLogin, text="Senha:", background=cor_de_fundo_geral)
        self.lb_espaco = Label(self.containerLogin, background=cor_de_fundo_geral) # apenas widget para colocar espaços em branco
        self.Check_senha = Checkbutton(self.containerLogin, text="Manter conectado", bg=cor_de_fundo_geral, activebackground=cor_de_fundo_geral)
        self.lb_mensagem = Label(self.containerLogin, background=cor_de_fundo_geral, foreground="#8B0000")

        # Input, entrada de dados
        self.ed_usuario = ttk.Entry(self.containerLogin)
        self.ed_senha = ttk.Entry(self.containerLogin)

        # Botão de entrar
        self.bt_entrar = ttk.Button(self.containerLogin, text="Entrar", command=self.func_entrar)

        # configuraçoes dos Widgets
        self.ed_usuario.config(width=35)
        self.ed_senha.config(width=35)
        self.ed_senha.config(show="*")
        self.lb_mensagem.config(font=('Verdana', '10'))

        # Foco da janela ao ser criada
        self.ed_usuario.focus_set()

        # Posicionamento Labels
        self.lb_usuario.grid(row=0, column=0, sticky=W)
        self.lb_senha.grid(row=3, column=0, sticky=W)
        self.lb_espaco.grid(row=1, column=0, pady=6)  # coloca um espaço entre o widget entry usuario e label senha
        self.lb_mensagem.grid(row=6, column=0)
        self.Check_senha.grid(row=5, sticky=W)

        # Posicionamento Enty
        self.ed_usuario.grid(row=1, column=0,  sticky=N)
        self.ed_senha.grid(row=4, column=0)

        # Posicionamento Buttons
        self.bt_entrar.grid(row=5, column=0, sticky=E, pady=10)

        # ----------- EVENTOS DOS WIDGETS -----------#
        self.ed_usuario.bind('<Key>', self.limpar_label)
        self.bt_entrar.bind('<Return>', self.keyEnter)
        self.ed_senha.bind('<Return>', self.keyEnter)

    def limpar_label(self, *ignore):
        self.lb_mensagem['text'] = ''

    def keyEnter(self, *ignore):
        self.func_entrar()

    def func_entrar(self):
        self.usuario = self.ed_usuario.get()
        self.senha = self.ed_senha.get()

        if ((self.usuario == 'admin') and (self.senha == 'admin')):
            # desabilida os frames, até entrar
            self.ed_usuario.config(state='disable')
            self.ed_senha.config(state='disable')

            global janela_login, decisao_entrar
            janela_login.destroy()
            decisao_entrar = True
        else:
            self.ed_usuario.config(state='normal')
            self.ed_usuario.config(state='normal')
            self.lb_mensagem["text"] = "Usuário e/ou senha incorreto"

            #setar focu para usuario novamente
            self.ed_usuario.focus_set()

# Variaveis globals
janela_estoque = None
Logar = None
decisao_entrar = False

# criação do obj
janela_login = Tk()
Logar = Entrar(janela_login)

# Propriedadesd da Janela
largura = 300
altura = 200

janela_login.maxsize(width=largura, height=altura) # tamanho máximo da janela
janela_login.minsize(width=largura, height=altura) # Tamanho mínimo da janela
janela_login.resizable(False, False) # Se a janela é redimensional em X e Y
janela_login.title("Login") # titulo da janela

# Cor de fundo da janela
janela_login.configure(background=cor_de_fundo_geral)

# Tamanho da janela e Onde ela deve ser posicionada ao ser criada
x = int(((Resolucao(0) / 2) - largura / 2))
y = int(((Resolucao(1) / 2) - altura/2))

janela_login.geometry("{width}x{height}+{Center_x}+{Center_y}".format(width=largura, height=altura, Center_x=x, Center_y=y))

# Executa a janela de login
janela_login.mainloop()

if decisao_entrar == True:
    del(decisao_entrar)
    from janela_estoque import *