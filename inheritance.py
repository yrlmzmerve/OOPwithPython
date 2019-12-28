#Inheritance

#parent ve child clası vardır
#child class parent classın attributelarını methodlarını kullanabilen alt closstır

#parent
class Animal:
    
    def __init__(self):
        print("animal is created")
        
    def toString(self):
        print("animal")
    
    def walk (self):
        print("animal walk")
        
#child
class Monkey(Animal): # Monkey clası Animal clasının childıdır
    
    def __init__(self):
        super().__init__() #parent clasının initilazır clasının içini child clasa aktarmasını sağlar
        print("monkey is created")
    
    def toString(self):
        print("monkey")
    
    #extend class
    def climb(self):
        print("monkey can climb")

class Bird(Animal):
    
    def __init__(self):
        super().__init__()
        print("bird is created")
    
    def toString(self):
        print("bird")
    
    def fly(self):
        print("bird can fly")

class Seagull(Bird):
    
    def __init__(self):
        super().__init__()
        print("Seagull is created")
    
    
#
m1 = Monkey()
m1.toString()
m1.walk()
m1.climb()
print("--")
b1 = Bird()
b1.toString()
b1.walk()
b1.fly()
print("--")
s1 = Seagull()












