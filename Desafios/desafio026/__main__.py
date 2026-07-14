from rich import inspect
from funcionarios import *

def main():
    f1 = FuncionarioHorista('Paulo', 25, 250)
    f2 = FuncionarioMensalista("Jose", 8500)
    f1.calc_sal()
    f1.analisar_salario()
    
    f2.calc_sal()
    f2.analisar_salario()
    
if __name__ == '__main__':
    main()