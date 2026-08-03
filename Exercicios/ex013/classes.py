class Mae:
    def __init__(self, nome:str = "Mamae") -> None:
        self.nome = nome
        
    def fazer_pudim(self):
        print(f"{self.nome} esta fazendo pudim com leite condensado e calda de caramelo")
        
    def fritar_coxinha(self):
        print(f"{self.nome} esta fritando coxinha de frango com catupiry")
        
class Filha(Mae):
    def fazer_pudim(self):
        print(f'{self.nome} faz pudim com leite ninho e com Nutella')

class Filho(Mae):
    def fritar_coxinha(self):
        print(f'{self.nome} frita coxinha na Air Fryer')