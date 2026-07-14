from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome:str, idade: int, cargo: str, setor: str):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setro = setor
    
    def bater_ponto(self):
        print(f'O funcionario {self.nome} bateu o ponto')