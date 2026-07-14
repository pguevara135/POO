from rich import print as rprint
from aluno import Aluno
from professor import Professor
from funcionatio import Funcionario

def __main__():
    
    a1 = Aluno("Jose", 17, "Informatica", "T01")
    a1.fazer_aniversario()
    a1.fazer_matricula()

    p1 = Professor("Paulo", 35, "Matematica", "Mestrado")
    p1.dar_aula()

    f1 = Funcionario("Maria", 28, "Secretaria", "Administrativo")
    f1.bater_ponto()

if __name__ == "__main__":
    rprint("\n[green]Iniciando o programa...\n[/]")
    __main__()