class Carteira:
    def __init__(self, valor:int|float):
        self.__saldo = valor
        
    def __str__(self):
        return f'Voce tem R${self.__saldo:.2f} na carteira'
        
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
        raise PermissionError('Voce nao tem autorizacao para altearar o saldo da carteira')
    
    def __eq__(self, outro):
        if self.__saldo == outro.__saldo:
            return True
        else:
            return False
    
    def __iadd__(self, valor:int|float):
        self.__saldo += valor
        return self
    
    def __isub__(self, valor:int|float):
        self.__saldo -= valor
        return self
    
    def __le__(self, outro):
        if self.__saldo <= outro.__saldo:
            return True
        else:
            return False