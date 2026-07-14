from abc import ABC, abstractmethod


class BebidaQuente(ABC):

    def preparar(self):
        print(f"Preparando o {self.bebida} quente...\n")

        self.ferver_agua()
        self.misturar()
        self.servir()

        print("\nBebida quente pronta!\n")

    def ferver_agua(self):
        print('1. Fervendo água a 100°C...')

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):

    bebida = 'Café'

    def misturar(self):
        print('2. Passando a água pelo coador com café moido...')

    def servir(self):
        print('3. Servindo o café em uma xicara pequena...')


class Cha(BebidaQuente):
    """Classe que representa a bebida quente Chá."""

    bebida = 'Chá'

    def misturar(self):
        print('2. Colocando o saquinho de chá na água quente...')

    def servir(self):
        print('3. Servindo o chá em uma caneca grande...')



class Leite(BebidaQuente):
    
    bebida = 'Leite'

    def misturar(self):
        print('2. Passando água pressurizada pelo leite para aquecer...')

    def servir(self):
        print('3. Servindo o leite quente em uma xicara grande...')
