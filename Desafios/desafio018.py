'''Modulo para fazer calculo de churrasco com amigos'''
from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.console import Group


class Churrasco:
    '''Recebe as informacoes de pessoas para o churrasco'''

    preco_Kg = 82.40
    consumoPessoa = 0.4

    def __init__(self, titulo, quant):
        #Atributo de instancia
        self.titulo = titulo
        self.quantidade = quant
        self.total_carne = 0
        self.custo_total = 0
        self.custo_pessoa = 0

    def calcular(self):
        '''Calcula o total de carne, valor por pessoa e valor total da compra '''
        self.total_carne = self.quantidade * self.consumoPessoa # tupe: ignore
        self.custo_total = self.preco_Kg * self.total_carne
        self.custo_pessoa = self.custo_total / self.quantidade

    def analisar(self):
        '''Retorna o calculo para quantidade de carne e valor por pessoa'''
        self.calcular()

        titulo = Text.from_markup(
            f'Analisando [green]{self.titulo}[/] com [blue]{self.quantidade} convidados[/]')

        participante = Text(
            f'Cada participante comera {self.consumoPessoa:.1f} kg e cada Kg custa R$ {self.preco_Kg:.2f}')

        carne = Text.from_markup(
            f'Recomento [bright_blue]comprar {self.total_carne:.3f} Kg[/] de carne')

        custo = Text.from_markup(
            f'O custo total sera de [green]R$ {self.custo_total:.2f}[/]')

        valor_por_pessoa = Text.from_markup(
            f'Cada pessoa pagara [bright_yellow]R$ {self.custo_pessoa:.2f}[/] para participar')

        conteudo = Group(titulo, participante, carne, custo, valor_por_pessoa)

        painel = Panel(
            conteudo,
            title=f'{self.titulo}',
            width=80
        )

        print(painel)


c1 = Churrasco("Churras dos Amigos", 15)
c2 = Churrasco("Festa do fim de ano", 80)

c1.analisar()
c2.analisar()
