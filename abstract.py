#Abstract Class / soyut
from abc import ABC, abstractmethod 
class Animal(ABC): #super class
    
    @abstractmethod
    def walk(self): pass

    def run(self): 
        print("run")

class Bird(Animal): #sub class
    
    def __init__(self):
        print("bird")
        
    def walk(self): pass
    
b1 = Bird()
