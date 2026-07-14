from rich import print as rprint
from rich.panel import Panel


class ControleRemoto:
    canal_min = 1
    canal_max = 6
    volume_min = 1
    volume_max = 5

    def __init__(self, canal: int = 1, volume: int = 1):
        self.canal_atual = canal
        self.volume_atual = volume
        self.ligado = False

    def ligar_desligar(self):
        self.ligado = not self.ligado

    def canal_menos(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_min:
                self.canal_atual = ControleRemoto.canal_max
            else:
                self.canal_atual -= 1

    def canal_mais(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_max:
                self.canal_atual = ControleRemoto.canal_min
            else:
                self.canal_atual += 1

    def volume_menos(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.volume_min:
                self.volume_atual -= 1

    def volume_mais(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.volume_max:
                self.volume_atual += 1

    def mostrar_tv(self):
        conteudo = ""
        if self.ligado == False:
            conteudo = f':prohibited:[red] A TV esta desligada[/]\n\n [green]Digite @ para Ligar[/]\n'
        else:
            conteudo = f'[green]Canal  = [/]'
            for canal in range(ControleRemoto.canal_min, ControleRemoto.canal_max + 1):
                if canal == self.canal_atual:
                    conteudo += f'[blue on yellow] {canal} [/]'
                else:
                    conteudo += f'{canal} '

            conteudo += f'\n[blue]Volume = [/]'
            for volume in range(ControleRemoto.volume_min, ControleRemoto.volume_max + 1):
                if volume < self.volume_atual:
                    conteudo += f'[black on cyan] [/]'
                elif volume == self.volume_atual:
                    conteudo += f'[black on cyan]{volume}[/]'
                else:
                    conteudo += f'[black on white] [/]'
            conteudo += f'\n\n[red]Digite @ par desligar[/] \n[cyan]Digite 0(Zero) para sair[/]\n'

        tv = Panel(conteudo, title='[ TV ]', subtitle='[ Controle Remoto ]', expand=False, border_style='blue')
        rprint(tv)


c = ControleRemoto()
while True:
    c.mostrar_tv()
    comando = str(input(f'< Ch-{c.canal_atual} >   - VOL-{c.volume_atual} +  '))
    match comando:
        case '0':
            break
        case '@':
            c.ligar_desligar()
        case "<":
            c.canal_menos()
        case ">":
            c.canal_mais()
        case "-":
            c.volume_menos()
        case '+':
            c.volume_mais()
        case _:
            pass
    
    print(f'\n * 10')