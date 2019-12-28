#Overriding

class Animal: #parent
    
    def toString(self):
        print("animal")
        
class Monkey(Animal): #subclass
    
    def toString(self):
        print("monkey")

a1 = Animal()
a1.toString()

m1 = Monkey()
m1.toString() # monkey clasıı overriding cagırıyor 

# parent classta tanımla olan method aynı isimde child classta da varsa child clastan oluşturulan nesne bu methodu aradıgında kendı methodundakı işlem gerçekleştirilir
# parent clastaki methodun işlevsiz olmasını sağlamaya overiding denir
# Monkey clasındakı toString metodu Animal clasındaki toString metodunu override eder