from animal import Animal

class Gato(Animal):
    
    def mover(self):
        print('Mover gato')
        
    def comer(self):
        super().comer()
        print('Gato come')