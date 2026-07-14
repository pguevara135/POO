from avaliacao import Avaliacao
from rich import print as rprint, inspect

def main():
    av1 = Avaliacao("Paulo", "Matematica", 9.7)
    av1.set_nota(10)
    
    rprint(f'{av1.nome} tirou nota {av1.get_nota()} na displina de {av1.disciplina}')
    # inspect(av1, private=True)
    
if __name__ == "__main__":
    main()