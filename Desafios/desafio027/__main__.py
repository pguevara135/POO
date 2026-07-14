from rich import inspect
from personagem_rpg import *

def main():
    p1 = Guerreiro('Pickachu', 1000)
    p2 = Mago("Gandalf", 1000)
    p1.receber_dano(100)
    
    p1.atacar(p2, 200)
    p2.atacar(p1, 200)
    
    p1.curar()
    p2.curar()

if __name__ == '__main__':
    main()