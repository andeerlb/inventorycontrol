#coding: utf-8

# Trabalhar todas excessões necessárias
def MenuExc(msg):
    while True:
        try:
            int(msg)
            if (int(msg) < 1 and int(msg) > 5):
                raise ValueError
            return int(msg)
        except ValueError:
            print("\nValor inválido...")
            msg = input("Escolha uma opção de 1 a 5, de acordo com o menu: ")

def PrecoExc(msg):
    while True:
        try:
            msg = msg.split(',')
            msg = '.'.join(msg)
            return float(msg)
        except ValueError:
                msg = input("\tValor incorreto, tente novamente: ")

def CodigoExc(msg):
    while True:
        try:
            return float(msg)
        except ValueError:
                msg = input("\tValor incorreto, tente novamente: ")

def ProdutoExc(msg):
    while True:
        try:
            list_msg = msg.split() # Fatia a string msg em partes, a partir do caracter espaço.
            for x in list_msg:
                if x.isalpha()==False: # isalpha verifica se x contém apenas letras
                    raise ValueError # Caso o valor extraido da lista list_msg aplicado em x for númerico, abre uma excessão.
            if msg.isspace() == True or msg == '':
                raise ValueError
            return msg # Caso toda string digita for validada como string ou conjunto de caracteres, retorna o valor passado para msg
        except (ValueError, AttributeError):
            if msg.isspace() != True and msg != '':
                print("\n\tVocê digitou '{}', porém este campo aceita apenas letras...".format(msg))
            else:
                print("\n\tVocê '{string}', porém este campo aceita apenas letras...".format(string="digitou ESPAÇO" if msg.isspace()==True else "pressionou ENTER"))
            msg = input("\tDigite o valor no campo novamente: ")