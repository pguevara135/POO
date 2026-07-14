from avaliacao import Avaliacao
from rich import print as rprint, inspect

def main():
    av1 = Avaliacao("Paulo", "Matematica")
    av1.nota = -11
    
    rprint(f'O aluno {av1.nome} tirou nota {av1.nota} na displina de {av1.disciplina}')
    inspect(av1, private=True)
    
if __name__ == "__main__":
    main()