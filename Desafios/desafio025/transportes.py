from abc import ABC, abstractmethod


class Transporte(ABC):

    def __init__(self, distancia: float):
        self.distancia = distancia
        self.frete: float = 0

    @abstractmethod
    def calc_frete(self) -> float:
        pass


class Moto(Transporte):  # ! Km ilimitado
    fator = 0.50

    def __init__(self, distancia: float):
        super().__init__(distancia)

    def calc_frete(self) -> float:
        self.frete = self.distancia * self.fator
        return f'R$ {self.frete:.2f}'


class Caminhao(Transporte):  # ! maior que 50 km
    fator = 1.20

    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self) -> float:
        if self.distancia > 50:
            self.frete = self.distancia * self.fator
            return f'R$ {self.frete:.2f}'
        else:
            return 'Distâncias minima que 50 km.'


class Drone(Transporte):  # ! Ate 10 km
    fator = 9.50

    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        if self.distancia > 10:
            return 'Raio maximo que 10 km.'
        else:
            self.frete = self.distancia * self.fator
            return f'R$ {self.frete:.2f}'
