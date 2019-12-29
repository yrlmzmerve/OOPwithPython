from abc import ABC, abstractmethod

class Shape(ABC):
    """
    Super Class & Abctract Class
    """
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    #overriding - polymorphism
    def toString(self):
        pass

class Square(Shape): #child class
    
    def __init__(self,edge):
        self.__edge = edge #private attr.
    
    def area(self):
        result = self.__edge**2
        print("Square Area: ", result )
        
    
    def perimeter(self):
        result = self.__edge*4
        print("Square Perimeter: ",  result)
        
    #overriding - polymorphism
    def toString(self):
        print("Square edge: ", self.__edge)
        
class Circle(Shape):
    #Constant variable
    PI = 3.14
    def __init__(self,radius):
        self.__radius = radius #private attr.
    
    def area(self):
        result = self.PI * self.__radius**2
        print("Circle Area: ", result )
        
    
    def perimeter(self):
        result = 2 * self.PI* self.__radius  # 2*pi*r
        print("Circle Perimeter: ",  result)
        
    #overriding - polymorphism
    def toString(self):
        print("Circle radius: ", self.__radius)
        
c = Circle(5)
c.area()
c.perimeter()
c.toString()

s = Square(5)
s.area()
s.perimeter()
s.toString()
    

    
    