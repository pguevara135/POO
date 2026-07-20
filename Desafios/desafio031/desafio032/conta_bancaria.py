from hashlib import sha256


class ContaBancaria:
    def __init__(self, id: int, titular: str = None, saldo: float = 0, chave: str = None):
        self._id = id
        self._titular = titular
        self.__saldo = saldo
        if chave is None:
            chave = self.pede_senha()
        self.__hash = sha256(chave.encode()).hexdigest()
        print(
            f'A conta de ID {self._id} de {self._titular} foi criada com sucesso.\nO saldo é de R$ {self.__saldo:.2f}.')

    def pede_senha(self):

        from pwinput import pwinput

        while True:
            senha = str(pwinput("Digite a senha da conta: ")).strip()
            if len(senha) < 6:
                print("A senha deve ter no mínimo 6 caracteres.")
            else:
                return senha

    def validar_senha(self, chave: str):
        usuario = sha256(chave.encode()).hexdigest()
        if usuario == self.__hash:
            return True
        else:
            return False

    def __str__(self):
        return f'Estado atual da conta: {self.__dict__}'

    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(
            f'Depósito de R$ {valor:.2f} foi efetuado com sucesso na conta {self._id} nome: {self._titular}.\nSaldo atual R$ {self.__saldo:.2f}.')

    def sacar(self, valor, chave: str = None):
        valor = abs(valor)

        if chave is None:
            chave = self.pede_senha()

        if self.validar_senha(chave):
            if valor > self.__saldo:
                print(
                    f"Saldo insuficiente para saque na conta {self._id} nome: {self._titular}.\nSaldo atual R$ {self.__saldo:.2f}.")
            else:
                self.__saldo -= valor
            print(
                f"O saque no valor de R$ {valor:.2f} foi efetuado com sucesso na conta {self._id} nome: {self._titular}.\nSaldo atual R$ {self.__saldo:.2f}.")
        else:
            print("Senha incorreta. Saque não efetuado.")
    
    @property
    def nome(self):
        return self._titular
    
    @nome.setter
    def nome(self, novonome: str = None):
        chave = self.pede_senha()
        
        if self.validar_senha(chave):
            if len(novonome) >= 3:
                self._titular = novonome
                print(f"Nome do titular da conta alterado com sucesso para {self._titular}.")
            else:
                print("O nome deve ter no mínimo 3 caracteres. Nome não alterado.")
        else:
            print("Senha incorreta. Nome não alterado.")
