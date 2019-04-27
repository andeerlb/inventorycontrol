# coding: utf-8

# INICIO de TUDO
from controle_estoque import *
from excessoes import *
import os

# Variaveis globais

# Menu princiapl
def menu_func():
    while True:
        os.system('cls')  # Limpar tela
        # Finalizar Controle de Estoque ou não
        while True:
            print()
            print("1 = Cadastrar novo produto")
            print("2 = Visualizar todos os produtos cadastrados")
            print("3 = Pesquisar produtos")
            print("4 = Excluir produto cadastrado")
            menu = MenuExc(input("5 = Finalizar execução: "))

            if (menu >= 1 and menu <= 5):  # Finaliza a verificação se foi digitada opção correta
                break
            else:
                print("\nEscolha uma opção de 1 a 5, de acordo com o menu")
                input("Tecle ENTER para prosseguir...")
                os.system('cls')  # Limpar tela

        os.system('cls')  # Limpar tela
        if menu == 1:
            cadastrar_estoque()
            input("\tDigite Enter para continuar")
        elif menu == 2:
            ler_estoque()
            input("\n\tDigite Enter para continuar")
        elif menu == 3:
            produto = input("\n\tDigite o CÓDIGO ou NOME do produto para localiza-lo: ")
            ler_estoque_avancado(produto)
            input("\n\tDigite enter para continuar")
        elif menu == 4:
            produto = input("\n\tDigite o CÓDIGO ou NOME do produto para localiza-lo: ")
            deletar_estoque(produto)
            input("\tTecle enter para continuar")
        # Finaliza a execução, dependendo da decisão
        elif menu == 5:
            break

# Informações sobre o produto
def cadastrar_estoque():
    codigo = Estoque.codigo_produto()
    print("\n\tCódigo: ", codigo)
    nome = ProdutoExc(input("\tDigite o nome do produto: "))
    preco_custo = PrecoExc(input("\tDigite o preço de custo: "))
    # Verifica se preço de custo é superior ao preço de venda, se for, pede pra redigitar o valor no campo
    while True:
        preco_venda = PrecoExc(input("\tDigite o preço de de venda: "))
        if preco_custo > preco_venda:
            print("\n\tVocê deve colocar o preço de venda similar ou maior que o preço de custo...")
        else:
            break

    fornecedor = ProdutoExc(input("\tDigite o fornecedor: "))
    Estoque(codigo, nome, preco_custo, preco_venda, fornecedor)  # Chama o objt estoque e passa os paremtros necessários
    print("\n\tCadastro realizado com sucesso!!")

# Efetua a leitura de todos os produtos do estoque
def ler_estoque():
    if estoque_vazio() == False:
        for codigo, valores in Estoque.estoque_dict.items():
            produto, custo, venda, fornecedor = valores
            info = """
            Código do produto: {codigo}
            Nome do Produto: {nome}
            Fornecedor: {fornecedor}
            Preço de custo: {preco_custo}
            Preço de venda: {preco_venda}
            """

            info = info.format(
                codigo=codigo,
                nome=produto,
                fornecedor=fornecedor,
                preco_custo= moeda(custo),
                preco_venda= moeda(venda)
            )
            print(info)
        else:
            estoque_vazio()

# Verifica se existe algum produto cadastrado
def estoque_vazio():
    if Estoque.estoque_dict == {}:
        print("\n\tEstoque Vazio.")
        # Caso não exista, pergunta ao cliente se ele quer efetuar um primeiro cadastro.
        menu = input("\tGostaria de cadastrar o primeiro produto? (S/N): ")
        while True:
            if (menu.lower() == 's'):
                # Inicia o cadastro do produto
                os.system('cls')
                cadastrar_estoque()
                # finaliza a função estoque_vazio()
                break
            elif (menu.lower() == 'n'):
                # finaliza o loop while e volta ao menu iniciar
                break
            else:
                print("\n\tPor favor, escolha uma opção...")
                print("\tS para sim ou N para não efetuar um cadastro de produto.")
                menu = input("\tGostaria de cadastrar um primeiro produto? (S/N): ")
    # Caso exista todos os produtos são listados.
    else:
        return False

# Moeda Pt-BR
def moeda(val):
    import locale
    locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252')
    val = locale.currency(val)
    return val

# Leitura avançada de estoque por código ou nome
def ler_estoque_avancado(nome_codigo):
    if estoque_vazio()==False:
        # Verifica se o código ou nome existe no cadastro
        if Estoque.pesquisa_avancada(nome_codigo) == False:
            os.system('cls')
            print("\n\tNão encontramos nenhum produto pela referencia: {}".format(nome_codigo))
        else:
            os.system('cls')
            val = Estoque.pesquisa_avancada(nome_codigo)
            for x in val:
                produto, custo, venda, fornecedor = Estoque.estoque_dict[x]
                info = """
                Código do produto: {codigo}
                Nome do Produto: {nome}
                Fornecedor: {fornecedor}
                Preço de custo: {preco_custo}
                Preço de venda: {preco_venda}
                """

                info = info.format(
                    codigo=x,
                    nome=produto,
                    fornecedor=fornecedor,
                    preco_custo= moeda(custo),
                    preco_venda= moeda(venda)
                )
                print(info)

# Função responsavel por deletador produtos encontrados no estoque
def deletar_estoque(nome_codigo):
    lista_estoques = Estoque.pesquisa_avancada(nome_codigo)
    if (lista_estoques == False):
        print('\n\tProduto Inexistente.')
    else:
        ler_estoque_avancado(nome_codigo)
        print('\t'+60*'-')
        x = CodigoExc(input("\tDigite o código do produto que você deseja deletar: "))
        while True:
            if x in lista_estoques:
                while True:
                    print('\t' + 60 * '-')
                    y = input("\n\tVocê realmente deseja deletar esse produto? (S/N): ")
                    if (y.lower() == 's'):
                        Estoque.deletar_produtos(int(x))
                        print('\t' + 60 * '-')
                        print("\n\tO produto foi deletado com sucesso.")
                        break
                    elif(y.lower() == 'n'):
                        print('\t' + 60 * '-')
                        print("\n\tVocê optou por não deletar o arquivo, voltaremos ao menu iniciar.")
                        break
                    else:
                        print("\tÉ necessário escolher uma opção. S=Sim ou N=Não")
                break
            else:
                x = CodigoExc(input("Digite o código de um dos produtos acima:"))

menu_func()