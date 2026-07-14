from rich import print
class Diario:
    def __init__(self, senhamestra='CeV!@'):
        self.__segredo = []
        self.__senha = senhamestra.strip()

    def escrever(self, msg):
        if isinstance(msg, str) and len(msg.strip()) > 0:
            self.__segredo.append(msg.strip())

    def ler(self, senha=None):
        if senha != self.__senha:
            raise PermissionError(f'Senha invalida. Voce nao pode ler o diario')
        else:
            print(f'[green]Diario Liberado![/green]')
            for segredo in self.__segredo:
                print(f'[blue]{segredo}[/blue]')

    @property
    def senha(self):
        raise PermissionError(
            f'Ninguem tem permissao para acessar a senha do diário.')

    @senha.setter
    def senha(self, nova_senha):
        if nova_senha.strip() == '':
            raise ValueError(f'A senha não pode ser vazia.')
        self.__senha = nova_senha.strip()
