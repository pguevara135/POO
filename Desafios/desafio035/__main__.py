from simulador import *

def main():
    a1 = PDF("arquivo", 1200000)
    a2 = DOC("arquivo", 5200000)
    abrir_arquivo(a1)
    abrir_arquivo(a2)

if __name__ == "__main__":
    main()