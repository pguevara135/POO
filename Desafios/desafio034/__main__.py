from funcionarios import *

def main():
    funcionarios = [
        Desenvolvedor("Pedro", 18000),
        Designer("Jose", 25000),
        Gerente("Mariana", 45000)
    ]
    
    for func in funcionarios:
        print(func)

if __name__ == "__main__":
    main()