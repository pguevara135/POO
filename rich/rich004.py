from rich import print
from rich import inspect

# inspect(int, all=True)
# print(int.__dict__)


class ContaBancaria:
    """
    Cria uma conta bancaria e permite fazer saques e depositos
    """

    def __init__(self, conta_id, nome, saldo=0):
        self.id = conta_id
        self.titular = nome
        self.saldo = saldo
        print(
            f'\nConta {self.id} criada com sucesso. Saldo atual de R$ {self.saldo:.2f}')

    def __str__(self):
        return f'A conta {self.id} de {self.titular} tem R$ {self.saldo:,.2f} de saldo'

    def depositar(self, valor):
        self.saldo += valor
        print(
            f'Deposito de \033[32mR$ {valor:,.2f} autorizado\033[0m na conta {self.id}\n')

    def sacar(self, valor):
        if valor > self.saldo:
            print(
                f'\033[31mSaldo Insuficiente\033[0m para saque no valor de R$ {valor}\n')
        else:
            self.saldo -= valor
            print(
                f'\033[31mSaque de R$ {valor:,.2f}\033[0m autorizado na conta {self.id}\n')


c = ContaBancaria(111, "Jose", 500)
inspect(c)
print(c.__getstate__())
print(c.sacar(500))
