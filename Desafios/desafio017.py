"""Module for creating product labels with Rich formatting."""
from rich import print as rprint  # criando o print formatado
from rich.panel import Panel
# from rich.text import Text
# from rich.console import Group


class Produto:
    '''Recebe os produtos e precos'''

    def __init__(self, produto, preco):  # type:ignore
        self.produto = produto
        self.preco = preco

    def __str__(self):
        return f'{self.produto} custa R$ {self.preco}'

    def etiqueta(self):
        '''Retorna formatado os produtos e precos'''
        conteudo = f'{self.produto.center(30, " ")}'
        conteudo += f'{"-" * 30}\n'
        precoformat = f'R$ {self.preco:,.2f}'
        conteudo += f'{precoformat.center(30, " ")}'
        etiqueta = Panel(conteudo, title='Produto', width=34)
        rprint(etiqueta)

        # produto = Text(self.produto, justify='center')
        # linha = "-" * 34
        # preco = Text(f'R$ {self.preco:.2f}', justify='center')

        # conteudo = Group(
        #     produto,
        #     linha,
        #     preco
        # )

        # painel = Panel(
        #     conteudo,
        #     title='Produto',
        #     width=40
        # )
        # print(painel)


p1 = Produto('iPhone 17 Pro Max', 25000.00)
p2 = Produto('Notebook Gamer', 8000)

p1.etiqueta()
p2.etiqueta()
