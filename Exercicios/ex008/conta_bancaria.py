class ContaBancaria:
    def __init__(self, id, nome, saldo) -> None:
        self.id = id #publico
        self._titular = nome #protegido
        self.__saldo   = saldo #privado
        print(f'A conta de id {self.id} de {self._titular} foi criada com sucesso.\nO saldo da conta é de R$ {self.__saldo:.2f}')
        
    def __str__(self) -> str:
        #return f'A conta {self.id} de {self._titular} tem R$ {self.__saldo:.2f} de saldo'
        return f'Estado atual de conta: {self.__dict__}'
    
    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f'Deposito de R$ {valor:.2f} foi efetuado na conta {self.id}\nSaldo atual {self.__saldo}')
        
    def sacar(self, valor):
        valor = abs(valor)
        self.__saldo -= valor
        print(f'O saque no valor de R$ {valor} foi efetuado com sucesso\nSaldo atual {self.__saldo}')