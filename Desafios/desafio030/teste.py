# import hashlib

# texto = 'Gafanhoto'

# cod = texto.encode('utf-8')
# hash = hashlib.sha256(cod).hexdigest()

# print(hash)

class Dog:  
    def __init__(self, name):  
        self.name = name

    def bark(self):  
        print(f"{self.name} says Woof!")  

my_dog = Dog("Rex")
print(my_dog.name)