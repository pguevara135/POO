from abc import ABC
from datetime import date

class Pessoa(ABC):
    
    def __init__(self, nome, nasc):
        self._nome = nome
        self._nascimento = None
        self.nascimento = nasc
    
    @property
    
    def nascimento(self):
        self._nascimento
    
    @nascimento.setter
    
    def nascimento(self, ano):
        if 1900 <= ano <=  date.today().year:
            self._nascimento = ano
        else:
            raise ValueError(f"Ano {ano} é inválido")
    
    @property
    
    def idade(self):
        return f'O aluno {self._nome} tem {date.today().year - self._nascimento} anos'
    
    @idade.setter
    
    def idade(self, valor):
        raise PermissionError("Voce não pode alterar a idade. Mude o ano de nascimento")
    

class Aluno(Pessoa):
    
    cursos_oficiais = ["ADM", "ADS", "ENG", "CONT"]
    
    def __init__(self, nome:str, nasc:int, curso:str):
        super().__init__(nome, nasc)
        self._curso = None
        self.curso = curso
        
    @property
    
    def curso(self):
        return self._curso
    
    @curso.setter
    
    def curso(self, curso:str):
        if curso in Aluno.cursos_oficiais:
            self._curso = curso
        else:
            self._curso = None
            raise ValueError(f"O curso {curso} não está na lista de cursos")
    
    def add_curso(self, curso:str):
        curso = curso.strip().upper()
        
        if curso in Aluno.cursos_oficiais:
            print(f"O curso {curso} já está cadastrado na base de dados")
            return
        elif 3 <= len(curso) <= 5:
            Aluno.cursos_oficiais.append(curso)
            print(f'Curso {curso} cadastrado com sucesso!')
        else:
            raise ValueError(f"Nome {curso} está fora do padrão de cadastro de cursos")