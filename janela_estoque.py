from tkinter import *
from win32api import GetSystemMetrics as Resolucao
from tkinter import messagebox

# Variaveis globais
cor_de_fundo_geral = '#3CB371'
cor_de_fundo_menu_lateral = "#cccccc"

class Estoque:
    def __init__(self, myParent):

        # Propriedades Widgets Menu Lateral
        align_text = 'W'
        padding_vertical = 10
        fonte = ("Verdana", "10")

        self.menu_lateral = Frame(myParent)
        self.menu_lateral.grid(pady=0)
        self.menu_lateral.config(background=cor_de_fundo_menu_lateral, padx=50)

        self.lb_add = Label(self.menu_lateral, text="Adicionar Produto", background=cor_de_fundo_menu_lateral, font=fonte)
        self.lb_add.grid(row=0, column=0, sticky=align_text, pady=padding_vertical)

        self.lb_remover = Label(self.menu_lateral, text="Remover Produto", background=cor_de_fundo_menu_lateral, font=fonte)
        self.lb_remover.grid(row=1, column=0, sticky=align_text,pady=padding_vertical)

        self.lb_pesquisar_all = Label(self.menu_lateral, text="Visualizar todos os produtos", background=cor_de_fundo_menu_lateral, font=fonte)
        self.lb_pesquisar_all.grid(row=2, column=0, sticky=align_text,pady=padding_vertical)

        self.lb_pesquisa_avancada = Label(self.menu_lateral, text="Pesquisar produtos", background=cor_de_fundo_menu_lateral, font=fonte)
        self.lb_pesquisa_avancada.grid(row=3, column=0, sticky=align_text,pady=padding_vertical)

        self.lb_editar_produto = Label(self.menu_lateral, text="Alterar produto", background=cor_de_fundo_menu_lateral, font=fonte)
        self.lb_editar_produto.grid(row=4, column=0, sticky=align_text,pady=padding_vertical)

        self.lb_deslogar = Label(self.menu_lateral, text="Finalizar sessão", background=cor_de_fundo_menu_lateral, font=fonte)
        self.lb_deslogar.grid(row=5, column=0, sticky=align_text, pady=padding_vertical)

        # eventos dos widgets
        #self.lb_deslogar.bind('<Button-1>', self.deslogar)
        self.lb_deslogar.place(y=350)

    def deslogar(self, ignore):
        global janela_estoque
        if messagebox.askokcancel("Sair", "Você deseja mesmo deslogar?"):
            janela_estoque.destroy()
            import janela_login

janela_estoque = Tk()
Estoque(janela_estoque)

# Propriedadesd da Janela
largura = 800
altura = 600

janela_estoque.maxsize(width=largura, height=altura) # tamanho máximo da janela
#janela_estoque.minsize(width=largura, height=altura) # Tamanho mínimo da janela
#janela_estoque.resizable(False, False) # Se a janela é redimensional em X e Y
janela_estoque.title("Controle de Estoque") # titulo da janela

# Cor de fundo da janela
janela_estoque.configure(background=cor_de_fundo_geral)

# Tamanho da janela e Onde ela deve ser posicionada ao ser criada
x = int(((Resolucao(0) / 2) - largura / 2))
y = int(((Resolucao(1) / 2) - altura/2))

janela_estoque.geometry("{width}x{height}+{Center_x}+{Center_y}".format(width=largura, height=altura, Center_x=x, Center_y=y))
janela_estoque.mainloop()