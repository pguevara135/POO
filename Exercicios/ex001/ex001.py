# Declaracao de classe
class Gafanhoto:
    '''Metodo Construtor'''
    def __init__(self):
        # Atributos de Instancia
        self.nome = ""
        self.idade = 0
    # Metodos de Instancia
    def aniversario(self):
        '''Metodos de Instancia'''
        self.idade += 1
    def mensagem(self):
        '''Metodos de Instancia'''
        return f"{self.nome} e Gafanhoto e tem {self.idade} anos de idade."

# Declaracao de Objetos

g1 = Gafanhoto()
g1.nome = "Julia"
g1.idade = 7
g1.aniversario()

print()
print(g1.mensagem())
print()

g2 = Gafanhoto()
g2.nome = "Paulo"
g2.idade = 57

print(g2.mensagem())
print()

g3 = Gafanhoto()
print(g3.mensagem())
print()
