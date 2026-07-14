from time import sleep

from rich import print as rprint


class Livro:
    '''Recebe o nome do livro e a quantidade de paginas'''

    def __init__(self, titulo, total_paginas):  # type: ignore
        self.titulo = titulo
        self.total_paginas = total_paginas
        self.pagina_atual = 1
        rprint(f'\n:open_book: [blue]Voce acabou de abrir o livro [red]{self.titulo}[/] que tem [green]{self.total_paginas} paginas[/] no total. Voce agora esta na pagina [yellow]pagina {self.pagina_atual}[/][/]\n')

    def avancar(self, quantidade=1):  # type: ignore
        '''Avanca paginas do livro'''
        destino = self.pagina_atual + quantidade

        if destino > self.total_paginas:
            destino = self.total_paginas
            ultrapassou = True
        else:
            ultrapassou = False
            # print(f'[red]Voce chegou ao final do livro {self.titulo}[/]')

        paginas_avancadas = 0

        while self.pagina_atual < destino:

            self.pagina_atual += 1
            paginas_avancadas += 1
            sleep(0.3)
            rprint(f'pag {self.pagina_atual} :arrow_forward: ', end="")
        rprint(f'[blue]Voce avancou {paginas_avancadas} paginas e agora esta na[/] [yellow]pagina {self.pagina_atual}[/]\n')
        if ultrapassou:
            rprint(
                f':closed_book: [red]Voce chegou ao final do livro {self.titulo}')


l1 = Livro("10 coisas que aprendi", 20)
l1.avancar(10)
l1.avancar(5)
l1.avancar(20)
