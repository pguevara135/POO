from classe import *

def main():
    
    a = Aluno("Julia", 2018, "ADM")
    print(a.idade)
    a.add_curso("Moda")
    
    # print(a.cursos_oficiais)

if __name__ == "__main__":
    main()