from rich import print as rprint
from rich.panel import Panel


class Gamer:
    '''Classe Gamer representa um jogador de videogame.'''

    def __init__(self, nome: str, nick: str):
        self.nome = nome
        self.nick = nick
        self.jogos_favoritos = list()

    def adicionar_favoritos(self, game: str):
        self.jogos_favoritos.append(game)
        self.jogos_favoritos.sort(key=str.lower)

    def ficha(self):
        titulo = f'Jogador[blue] <= {self.nick.upper()} =>[/]\n'
        conteudo = f'\nNome Real:[black on white] {self.nome} [/]\n'
        conteudo += f'\nJogos Favoritos\n'
        for jogo in enumerate(self.jogos_favoritos):
            conteudo += f'\n:video_game: -[blue] {jogo[1]}[/]'

        painel = Panel(conteudo, title=titulo, expand=False)
        rprint(painel)


j1 = Gamer('João Cabrito', 'brutao')
j1.adicionar_favoritos('GTA V')
j1.adicionar_favoritos('Minecraft')
j1.adicionar_favoritos('battlefield 2042')
j1.ficha()
