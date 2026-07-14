# Declaracao de classe
class Gafanhoto:
    """
Essa classe cria um Gafanhoto, que uma pessoa ue tem nome e idade.
Para criar uma nova pessoa use 
variavel Gafanhoto(nome, idade)

    """

    def __init__(self, nome='vazio', idade=0):
        # Atributos de Instancia
        self.nome = nome
        self.idade = idade
    # Metodos de Instancia

    def aniversario(self):
        '''Metodos de Instancia'''
        self.idade += 1

    def __str__(self):
        return f'{self.nome} e Gafanhoto e tem {self.idade} anos de idade'
    
    def __getstate__(self):
        return f'Estado: nome = {self.nome} ; idade = {self.idade}'
    
# Declaracao de Objetos


g1 = Gafanhoto('Julia', 7)
g1.aniversario()

print()
print(g1)
print()

print(g1.__dict__)
print(g1.__getstate__())
print(g1.__class__)
print()

g2 = Gafanhoto('Paulo', 57)
print(g2)
print(g2.__getstate__())