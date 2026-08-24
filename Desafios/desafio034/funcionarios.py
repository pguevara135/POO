from abc import ABC, abstractmethod


class Funcionario(ABC):
    def __init__(self, nome: str = None, salario: float = 1.621):
        self.nome = nome
        self.__salario = salario

    @abstractmethod
    def calcularBonus(self):
        pass

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, valor: float | None = None):
        if valor is None:
            raise ValueError("Salário não pode ser None")
        else:
            if valor >= self.__salario:
                self.__salario = valor
            else:
                raise ValueError("Voce nao pode reduzir o valor do salario")

    def __str__(self):
        return f"{self.nome} recebe R$ {self.salario:,.2f} e por ser {self.__class__.__name__} o bonus sera de R$ {self.calcularBonus():,.2f}"


class Gerente(Funcionario):
    def calcularBonus(self):
        return self.salario * 0.15


class Designer(Funcionario):
    def calcularBonus(self):
        return self.salario * 0.08


class Desenvolvedor(Funcionario):
    def calcularBonus(self):
        return self.salario * 0.10
