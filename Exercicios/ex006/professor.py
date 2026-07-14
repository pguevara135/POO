from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome: str, idade: int, especialidade: str, nivel: str):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel
    
    def dar_aula(self):
        print(f'O professor {self.nome} comecou a aula de {self.especialidade}')