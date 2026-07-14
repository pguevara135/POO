from rich import print as rprint


class Caneta:
    '''Escreve um text com a cor ca caneta escolhida'''

    def __init__(self, cor: str = 'azul'):
        escolha = ''
        match cor.lower().strip():
            case 'azul':
                escolha = '[blue]'
            case 'vermelho' | 'vermelha':
                escolha = '[red]'
            case 'verde':
                escolha = '[green]'
            case 'amarelo':
                escolha = '[yellow]'
            case _:
                escolha = '[white]'

        self.cor = escolha
        self.tampada = True

    def escrever(self, msg: str):
        if self.tampada:
            rprint(
                f':prohibited: A {self.cor} caneta[/] está tampada! Desculpe, não posso escrever.', end='')
        else:
            rprint(f'{self.cor} {msg}[/]', end='')

    def quebrar_linha(self, qtd: int = 1):
        print('\n' * qtd, end='')

    def tampar(self):
        self.tampada = True

    def destampar(self):
        self.tampada = False


c1 = Caneta('azul')
c2 = Caneta('vermelho')
c3 = Caneta('verde')

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever('Olá, mundo!')
c1.quebrar_linha(2)
c2.escrever('Caneta vermelha')
c2.quebrar_linha(5)
c3.escrever('Caneta verde')
