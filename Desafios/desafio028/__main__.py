from termostato import Termostato

def main():
    t = Termostato()
    try:
        t.temperatura = 25
    except ValueError as e:
        print(f'Hou um problema: {e}')
    
    print(f'A temperatura atual e de {t.ftemperatura}')

if __name__ == '__main__':
    main()