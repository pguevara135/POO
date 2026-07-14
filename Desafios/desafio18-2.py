from rich import print
from rich.panel import Panel


class churrasco:
    # Atributo de Classe
    consumo_padrao = 0.400  # Consumo medio por pessoa
    preco_kg = 82.40  # Custo do kg da carne

    def __init__(self, titulo, qtd):
        self.titulo = titulo
        self.quantidade = qtd

    def __str__(self) -> str:
        return f'Esse e o {self.titulo} com {self.quantidade} participantes.'

    def qtde_carne(self) -> float:
        return churrasco.consumo_padrao * self.quantidade

    def custo_total(self) -> float:
        return self.qtde_carne() * churrasco.preco_kg

    def custo_individual(self) -> float:
        return self.custo_total() / self.quantidade

    def analisar(self):
        conteudo = f'Analisando [green]{self.titulo}[/] com [blue]{self.quantidade} convidados[/]'
        conteudo += f'\nCada partipante comera {churrasco.consumo_padrao:.3f} kg e cada kg custa R$ {churrasco.preco_kg:.2f}'
        conteudo += f'\nRecomendo [blue]comprar {self.qtde_carne():.3f} kg[/] de carne'
        conteudo += f'\nO custo total sera de [green]R$ {self.custo_total():.2f}[/]'
        conteudo += f'\nCada pessoa pagara [yellow]R$ {self.custo_individual():.2f}[/] para participar.'
        painel = Panel(conteudo, title=self.titulo)
        print(painel)


c1 = churrasco("Churras dos Amigos", 15)
c2 = churrasco('Festa do fim de ano', 80)
c1.analisar()
c2.analisar()