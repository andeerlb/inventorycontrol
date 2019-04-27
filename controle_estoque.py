#coding: utf-8

# Controle de Estoque
class Estoque:
    estoque_dict = {1234: ['a', 1,1,'a'], 4321: ['b', 1,1,'b'], 1324: ['c', 1,1,'c'], 1235: ['a', 2,2,'a']}  # contém todos os produtos com seus devidos atributos.
    # método construtor
    def __init__(self, _codigo, _produto, _preco_de_custo, _fornecedor, _preco_de_venda):
        self._codigo, self._preco_de_custo, self._fornecedor, self._preco_de_venda = 0,0,0,0
        self._produto = ''
        self.estoque_func = (_codigo, _produto, _preco_de_custo, _fornecedor, _preco_de_venda)

    @property
    def estoque_func(self):
        return self.estoque_dict

    # Escreve os parametros no dicionário
    @estoque_func.setter
    def estoque_func(self, val):
        self._codigo, self._produto, self._preco_de_custo, self._preco_de_venda, self._fornecedor = val
        self.estoque_dict.update({int(self._codigo): [self._produto.title(), self._preco_de_custo, self._preco_de_venda, self._fornecedor.title()]})

    # Cria um valor númerico conténdo 4 casas, cada casa recebe um valor de 1 a 10 eleatóriamente
    @staticmethod
    def valor_rondom():
        from random import sample
        result = sample(range(1, 10), 4)
        result = ''.join(str(x) for x in result)
        return result

    # Verifica se o valor criando no método valor_rondom() já existe como chave primaria no dict, se existir, altera o valor
    @staticmethod
    def codigo_produto():
        while True:
            valor = Estoque.valor_rondom()
            if (valor in list(Estoque.estoque_dict)):
                Estoque.valor_rondom()
            else:
                return valor

    # Pesquisar produtos por chave primeira(codigo) e/ou nome do produto
    @staticmethod
    def pesquisa_avancada(produto):
        lista_produtos = []
        produto = str(produto).lower()
        for valor, item in Estoque.estoque_dict.items():
            lista_pesq = [str(valor), str(item[0].lower())]
            if produto in lista_pesq: # verifica se o campo prodouto contém na lista lista_pesq
                lista_produtos.append(int(valor)) # se contér, retorna a chave primaria e finaliza a função pesquisa_avancada()
        if lista_produtos != []:
            return lista_produtos
        else:
            return False

    # Método responsável por apagar produtos escolhidos pelo funcionário
    @staticmethod
    def deletar_produtos(produto):
        del(Estoque.estoque_dict[produto])
