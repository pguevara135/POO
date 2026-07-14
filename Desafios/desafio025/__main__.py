from transportes import Caminhao, Drone, Moto
from rich import print as rprint
from rich.table import Table

# 0d8686
def main():
    distancia = 30

    # entrega = Drone(distancia)
    # print(f'Frete de {entrega.__class__.__name__} em {distancia} km = {entrega.calc_frete()}') #! Para mostrar o nome da classe pode ser tambem {type(entrega)__nome__}

    viagem: list[Moto | Caminhao | Drone] = [Moto(distancia), Caminhao(distancia), Drone(distancia)]

    tabela = Table(title='Tabela de Fretes')
    tabela.add_column("Distancia")
    tabela.add_column('Tipo')
    tabela.add_column("Frete")

    for item in viagem:
        tabela.add_row(
            f'{distancia} km', f'{type(item).__name__}', f'{item.calc_frete()}')

    rprint(tabela)


if __name__ == "__main__":
    main()
