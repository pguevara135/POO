from diario import Diario
from rich import print as rprint, inspect

def main():
    meudiario = Diario()
    meudiario.escrever('Hoje eu aprendi sobre classes em Python.')
    meudiario.escrever('Também aprendi sobre encapsulamento e propriedades.')
    
    try:
        meudiario.ler('CeV!@')  # Senha correta
    except PermissionError as e:
        rprint(f'[red]{e}[/red]')
    
    # inspect(meudiario, private=True)

if __name__ == '__main__':
    main()