from rich import print as rprint
from classex005 import Aluno, Professor, Funcionario

def __main__():
    

    a1 = Aluno("Jose", 17, "Informatica", "T01")
    a1.fazer_aniversario()
    a1.fazer_matricula()

    p1 = Professor("Paulo", 35, "Matematica", "Mestrado")
    p1.dar_aula()

    f1 = Funcionario("Maria", 28, "Secretaria", "Administrativo")
    f1.bater_ponto()

if __name__ == "__main__":
    rprint("\n[blue]Iniciando o programa...\n[/]")
    __main__()