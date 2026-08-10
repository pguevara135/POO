class Porta:
    def abrir(self):
        print('Girar a macaneta e empurrar a porta para abrir.')
    
class Empresa:
    def abrir(self):
        print('Va ao portal do empreendedor leve a documentacao para abrir uma empresa')
    
class Ovo:
    def abrir(self):
        print('Quebre a casca do ovo e coloque em uma frigideira para fritar')

class Pedra:
    pass

# METODO PYTHONICO POLIFORMICO DUCK TYPING

def tentar_abrir(obj):
    try:
        obj.abrir()
    except:
        print(f"Encontrei problemas ao tentar abrir {obj.__class__.__name__}") 