from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def mover(self):
        pass
    
    @abstractmethod
    def comer(self):
        print('Animal come')