from abc import ABC, abstractmethod
import locale

# Set the locale for currency formatting
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class Pagamento(ABC):
    
    def __init__(self):
        self._valor = None
        
    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self, valor: float):
        if valor > 0:
            self._valor = valor
        else:
            raise ValueError(f"O pagamnento não pode ser menor ou igual a zero. Valor informado: {valor}")
        
    @property
    def fvalor(self):
        return locale.currency(self._valor, grouping=True)

    @abstractmethod
    def pagar(self):
        pass
    
class Boleto(Pagamento):
    def pagar(self, valor: float):
        try:
            self.valor = valor
            print(f"Pagamento de {self.fvalor} via Boleto realizado com sucesso!")
        except Exception as e:
            print(f"Falha no pagamento de {self.fvalor} via Boleto. Erro: {e}")
        

class Pix(Pagamento):
    def pagar(self, valor: float):
        try:
            self.valor = valor
            return f"Pagamento de {self.fvalor} via Pix realizado com sucesso!"
        except Exception as e:
            return f"Falha no pagamento de {self.fvalor} via Pix. Erro: {e}"

class Cartao(Pagamento):
    def pagar(self, valor: float):
        try:
            self.valor = valor
            return f"Pagamento de {self.fvalor} via Cartão realizado com sucesso!"
        except Exception as e:
            return f"Falha no pagamento de {self.fvalor} via Cartão. Erro: {e}"
            
def finalizar_pagamento(pagamento: Pagamento, valor: float):
    print(pagamento.pagar(valor))