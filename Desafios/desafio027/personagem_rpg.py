import random
from abc import ABC, abstractclassmethod
from rich import print as rprint


class Personagem(ABC):
    def __init__(self, nome: str, vida: int):
        self.nome: str = nome
        self.vida: int = vida
        self.golpes: list = []

    def atacar(self, alvo, forca = 100):
        if self.vida > 0 and alvo.vida > 0:
            golpe = self.golpes[random.randrange(0, len(self.golpes))]
            
            rprint(f'[green]{self.nome}[/]({self.vida}) atacou [red]{alvo.nome}[/]({alvo.vida}) com um [magenta]{golpe}[/] com forca de [yellow]{forca}[/]\n')
            alvo.receber_dano(forca)
        else:
            rprint(f"[red]O ataque {self.nome} -> {alvo.nome} nao pode acontecer[/]\n")

    def receber_dano(self, dano):
        fator = random.randint(0, dano)
        self.vida -= fator
        if self.vida < 0:
            self.vida = 0
        rprint(f'[blue]{self.nome}[/] recebeu [red]dano de {fator}[/]\n')

    @abstractclassmethod
    def curar(self):
        pass


class Guerreiro(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Soco', 'Golpe de machado', 'Pulo Giratorio']

    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        rprint(f'[blue]{self.nome}[/] enrolou uma atadura nos ferimentos e recuperoou [gree]{fator}[/] pontos de vida\n')


class Mago(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Bola de Fogo', 'Raio de Luz', 'Magia Estatica']

    def curar(self):
        fator = random.randint(0, 100)
        rprint(f'[blue]{self.nome}[/] fez uma magia de cura e recuperou [green]{fator}[/] pontos de vida')
