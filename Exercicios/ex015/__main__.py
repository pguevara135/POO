from classes import *

def main():
    c1 = Carteira(400)
    c2 = Carteira(500)
    print(c1 == c2)
    
    
    c1 += 200  # Tentativa de adicionar valor, deve gerar um erro
    print(c1)
    
    c1 -= 150
    print(c1)
    
    print(c1 <= c2)

if __name__ == "__main__":
    main()