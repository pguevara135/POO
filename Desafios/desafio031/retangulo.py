class Retangulo:
    def __init__(self, base = 1, altura = 1):
        self._base = None
        self._altura = None
        self._area = None
        
        self.base = base
        self.altura = altura
        
    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, valor):
        if not isinstance(valor, int) and not isinstance(valor, float):
            raise TypeError('O valor da base deve ser um numero')
        if valor < 0:
            raise ValueError('O valor da base deve ser maior que zero')
        else:
            self._base = valor
            
    
    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, valor):
        if not isinstance(valor, int) and not isinstance(valor, float):
            raise TypeError('O valor da altura deve ser um numero')
        if valor < 0:
            raise ValueError('O valor da altura deve ser maior que zero')
        else:
            self._altura = valor
    
    @property
    def area(self):
        self._area = self._base * self._altura
        return self._area
    
    @area.setter
    def area(self):
        raise PermissionError('Area nao pode ser alterada diretamente. Use base e altura para calcular a area.')
    
    @property
    def medidas(self):
        return f'Base = {self.base} \nAltura = {self.altura} \nArea = {self.area}'
    
    @medidas.setter
    def medidas(self, valores:tuple):
        if not isinstance(valores, tuple):
            raise TypeError('As medidas devem ser indomradas dentro de uma tupla')
        if len(valores) != 2:
            raise SyntaxError('Informe uma tuplas com dois valores')
        if isinstance(valores[0], int) or isinstance(valores[0], float):
            self.base = valores[0]
        else:
            raise TypeError('O valor da base deve ser um numero')
        if isinstance(valores[1], int) or isinstance(valores[1], float):
            self.altura = valores[1]
        else:
            raise TypeError('O valor da altura deve ser um numero')