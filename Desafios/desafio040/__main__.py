from usuarios import *

def main():
    u = [Usuario('Pedro', 'hjhjkhkjh@hotmail.com'), Usuario('Maria', 'maria@hotmail.com')]
    a = [Aluno('Pedro', 'Python', '3º'), Aluno('Maria', 'Python', '3º')]
    
    exportar_dados(JSON(), u)
    exportar_dados(XML(), a)


if __name__ == '__main__':
    main()