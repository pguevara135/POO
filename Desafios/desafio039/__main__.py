from validador import *

def main():
    validar_dado(Usuario(), "paulo")
    validar_dado(Email(), "paulo123@gmail.com")
    validar_dado(Senha(), "Adef123!@")

if __name__ == '__main__':
    main()
 