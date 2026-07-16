from retangulo import Retangulo


def main():

    r = Retangulo(7, 4)
    try:
        r.base = 12
        r.altura = 4
        r.medidas = (8, 12)
    except Exception as e:
        print(f'Ocorreu um erro de tipo: {type(e).__name__}: {e}')

    print(r.medidas)


if __name__ == '__main__':
    main()
