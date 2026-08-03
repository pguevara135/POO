from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome:str = ""):
        self.nome = nome
    
    @abstractmethod
    def emitir_som(self):
        print(f"{self.nome} e {self.__class__.__name__} e esta emitindo som")

class Pato(Animal):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer quack quack")

class Cachorro(Animal):
    
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer au au au")
        
class Sptizer(Cachorro):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer au au au au au au au")

class Pitbull(Cachorro):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer Ruf Ruf Ruf")

class Gato(Animal):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer miau miau")

class Galinha(Animal):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer có có có")