"""Module for employee presentation using rich formatting."""
from rich import print
from rich import inspect


class Funcionario:
    '''Class representa os funcionario e cargos dentro da empresa'''
    #? Atributos de Classe
    empresa = "Curso em Video"

    def __init__(self, nome, setor, cargo):
        #? Atributos de instancia
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self) -> str:
        '''Retorna a apresentacao do funcionario'''
        return f':handshake: Ola, sou [blue]{self.nome}[/blue] e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa}\n'


c1 = Funcionario('Maria', 'Administracao', 'Diretora')

c2 = Funcionario('Pedro', 'TI', 'Programador')
print(c1.apresentacao())

print(c2.apresentacao())

# inspect(c1, methods=True, dunder=True)
# inspect(Funcionario, all=True)
