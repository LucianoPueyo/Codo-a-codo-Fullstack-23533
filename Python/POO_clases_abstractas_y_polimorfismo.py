from abc import ABC, abstractmethod

#ABC = Abstract Base Class
class Animal(ABC):
    @abstractmethod
    def mover(self):
        pass

class Perro(Animal):
    def mover(self):
        print("caminando en 4 patas")

class Pez(Animal):
    def mover(self):
        print("Nadando por el mar")

#animal1 = Animal()

perro1= Perro()
pez1 = Pez()

perro1.mover()
pez1.mover()

