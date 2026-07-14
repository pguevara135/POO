from abc import ABC, abstractmethod
from rich import print as rprint
from rich.panel import Panel


class Funcionario(ABC):

    salario_minimo = 1612
    desconto_inss = 7.5

    def __init__(self, nome: str):
        self.nome = nome
        self.salario_bruto = 0
        self.salario = 0

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_salario(self):
        base = self.salario / Funcionario.salario_minimo
        mensagem = f'\nO salario de [blue]{self.nome}[/] um [margenta]({self.__class__.__name__})[/] é de [green]R$ {self.salario:.2f}[/] e corresponde a [yellow]{base:.1f} salarios minimo[/]\n'
        painel = Panel(mensagem, title='Analise de Salario', width=50)
        rprint(painel)


class FuncionarioHorista(Funcionario):

    def __init__(self, nome: str, valor_hora: float = 7.37, qtd_horas: int = 220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.qtd_horas = qtd_horas
        self.salario_bruto = self.valor_hora * self.qtd_horas

    def calc_sal(self):
        self.salario = self.salario_bruto - \
            (self.salario_bruto * self.desconto_inss / 100)
        

    


class FuncionarioMensalista(Funcionario):

    def __init__(self, nome: str, salario_bruto = Funcionario.salario_minimo):
        super().__init__(nome)
        self.salario_bruto = salario_bruto
        
        
    def calc_sal(self):
        self.salario = self.salario_bruto - (self.salario_bruto * self.desconto_inss / 100)