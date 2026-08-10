from classes import *

def main():
    x = Analisador()
    x.analisar(10)
    x.analisar("Olá, mundo!")
    x.analisar(3.14)
    x.analisar([1, 2, 3])
    x.analisar({"chave": "valor"})
    x.analisar(None)  # Testando com um valor que não é tratado
    x.analisar(max([4, 9, 7]))
    x.analisar(len([4, 9, 7]))

if __name__ == "__main__":
    main()