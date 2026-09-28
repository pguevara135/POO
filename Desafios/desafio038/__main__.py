from carrinho import *

def main():
    p1 = Produto("Notebook", 8000)
    p2 = Produto("Mouse", 420.0)
    p3 = Produto("Teclado", 150.0)
    
    c1 = Carrinho()
    c2 = Carrinho()
    
    c1 = c1 + p1
    c1 = c1 + p2
    c1 = c1 + p3
    
    c2 = c2 + c1
    
    print(f'Carrinho 1: {c1}')
    print(f'Carrinho 2: {c2}')
   

if __name__ == "__main__":
    main()