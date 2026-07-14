from rich import print, inspect

class Pessoa:
    def __init__(self,nome = "", idade = 0):
        self.nome = nome
        self.idade = idade
    
    def fazer_aniversario(self):
        self.idade += 1
    
class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma
    
    def fazer_matricula(self):
        print(f'O aluno {self.nome} fez a matricula')

class Professor(Pessoa):
    def __init__(self, nome: str, idade: int, especialidade: str, nivel: str):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel
    
    def dar_aula(self):
        print(f'O professor {self.nome} comecou a aula de {self.especialidade}')

class Funcionario(Pessoa):
    def __init__(self, nome:str, idade: int, cargo: str, setor: str):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setro = setor
    
    def bater_ponto(self):
        print(f'O funcionario {self.nome} bateu o ponto')
    
a1 = Aluno("Paulo", 17, "Informatica", "T01")
a1.fazer_aniversario()
a1.fazer_matricula()
# print(a1.__dict__)
inspect(a1, methods=True)

p1 = Professor("Paulo", 35, "Matematica", "Mestrado")
p1.dar_aula()
inspect(p1, methods=True)

f1 = Funcionario("Maria", 28, "Secretaria", "Administrativo")
f1.bater_ponto()
inspect(f1, methods=True)