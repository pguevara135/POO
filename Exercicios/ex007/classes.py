from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar(self):
        pass


class Aluno(Pessoa):
    def __init__(self, nome: str, idade: int, curso: str, turma: str):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f'O aluno {self.nome} fez a matricula')
    
    def estudar(self):
        print(f'O aluno {self.nome} esta estudando, {self.curso} na turma {self.turma}')


class Professor(Pessoa):
    def __init__(self, nome: str, idade: int, especialidade: str, nivel: str):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f'O professor {self.nome} esta dando aula de {self.especialidade}')
    
    def estudar(self):
        print(f'O professor {self.nome} esta dando aula de {self.especialidade} para melhorar suas habilidades')


class Funcionario(Pessoa):
    def __init__(self, nome: str, idade: int, cargo: str, setor: str):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f'O funcionario {self.nome} bateu o ponto')
        
    def estudar(self):
        print(f'O funcionario {self.nome} esta estudando para melhorar suas habilidades no cargo de {self.cargo}')
