class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco
    
    def __str__(self) -> str:
        return f"{self.nome} {formata_dinheiro(self.preco)}"
        
        
class Carrinho:
    
    def __init__(self, produtos: list = None):
        self.produtos = produtos if produtos else []
    
    @property
    def total(self):
        return sum(p.preco for p in self.produtos)
    
    def __add__(self, outro):
        if isinstance(outro, Produto):
            return Carrinho(self.produtos + [outro])
        elif isinstance(outro, Carrinho):
            return Carrinho(self.produtos + outro.produtos)
        else:
            raise TypeError("Voce tentou adincionar um tipo inválido ao carrinho")
    
    def __str__(self) -> str:
        linha = "\n" + "-" * 40 + "\n"
        itens = "\n".join(str(p) for p in self.produtos)
        return f"{linha}{itens}{linha}Total: {formata_dinheiro(self.total)}{linha}{linha}"


def formata_dinheiro(valor: float):
    import locale
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    return locale.currency(valor, grouping=True)