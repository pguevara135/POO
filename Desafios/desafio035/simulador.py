from abc import ABC, abstractmethod

class Arquivo(ABC):
    def __init__(self, nome_arquivo:str, extensao:str, tamanho:int = 0):
        self.arquivo = nome_arquivo
        self._extensao = None
        self.tamanho = tamanho
        self.extensao = extensao

    @abstractmethod
    def abrir(self):
        pass
    
    @property
    def extensao(self):
        return self._extensao
    
    @extensao.setter
    def extensao(self, extensao:str):
        formatos =["pdf", "doc", "docx"]
        extensao = extensao.lower().strip()
        if extensao in formatos:
            self._extensao = extensao
        else:
            raise ArithmeticError(f"O Aquivo {self.arquivo} não é suportado. Formatos aceitos: {formatos}")
    
    @property    
    def nome_completo(self):
        return f"{self.arquivo}.{self.extensao} ({self.tamanho/1000000} MB)"
        

class PDF(Arquivo):
        
    def __init__(self, nome_arquivo:str, tamnanho:int):
        super().__init__(nome_arquivo, "pdf", tamnanho)
            
    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} no Adobe Reader")
    
class DOC(Arquivo):
    def __init__(self, nome_arquivo:str, tamanho:int):
        super().__init__(nome_arquivo, "docx", tamanho)
            
    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} no Microsoft Word")

def abrir_arquivo(arquivo:Arquivo):
    arquivo.abrir()