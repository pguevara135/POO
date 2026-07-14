from credencial import Credencial

def main():
    cred = Credencial()
    cred.senha = str(input('Digite a senha: '))
    print(cred.senha)
    
    cred.validar(' CeV!@')

if __name__ == '__main__':
    main()