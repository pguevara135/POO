from rich import print
from rich.panel import Panel

class Mensagem:
    def __init__(self, texto: str = "", tipo: str = "aviso", icone: str = ":speech_balloon:"):
        self._mensagem = texto
        self._tipo = tipo
        self._icone = icone
    
    def mostrar(self):
        texto = Panel(self._mensagem, title=f"{self._icone} {self._tipo.upper()} {self._icone}", expand=False, style="bold green")
        print(texto)



class Erro(Mensagem):
    def __init__(self, texto: str = ""):
        super().__init__(texto, tipo="Erro", icone=":x:")
    
    def mostrar(self):
        texto = Panel(self._mensagem, title=f"{self._icone} {self._tipo.upper()} {self._icone}", expand=False, style="bold red")
        print(texto)

class Aviso(Mensagem):
    def __init__(self, texto: str = ""):
        super().__init__(texto, tipo="Aviso", icone=":warning:")
        
    def mostrar(self):
        texto = Panel(self._mensagem, title=f"{self._icone} {self._tipo.upper()} {self._icone}", expand=False, style="bold yellow")
        print(texto)