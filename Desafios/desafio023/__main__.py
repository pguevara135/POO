from rich import print
from poligono import *

def main():
    p1 = Quadrado(20)
    p2 = Circulo(12)
    
    print(f'Perimetro = {p1.perimetro():.1f} - Area = {p1.area():.1f}')
    print(f'Perimetro = {p2.perimetro():.1f} - Area = {p2.area():.1f}')
    
if __name__ == "__main__":
    main()