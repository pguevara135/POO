from functools import singledispatchmethod

class Analisador:
    
    @singledispatchmethod
    
    def analisar(self, valor):
        print(f'Nao foi possivel analisar o valor: {valor}')
        
    @analisar.register
    def _(self, valor:int):
        print(f"Analisando o valor: {valor} e um numero inteiro.")
        
    @analisar.register
    def _(self, valor:float):
        print(f"Analisando o valor: {valor} e um numero decimal.")
        
    @analisar.register
    def _(self, valor:str):
        print(f"Analisando o valor: {valor} e uma string.")
        
    @analisar.register
    def _(self, valor: tuple|list|dict):
        print(f"Analisando o valor: {valor} e uma colecao.")