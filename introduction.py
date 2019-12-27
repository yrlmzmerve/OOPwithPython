# %% classes

class Employee (object):
    #attribute
    #behaviour
    pass

employee1 = Employee() #classtan nesne oluşturma

# %% atribute

class Footballer:
    football_club="Barcelona"
    age=30
     
    pass

f1 = Footballer()

print(f1)
print(f1.age)
print(f1.football_club)

f1.football_club = "real madrid"
print(f1.football_club)

# %% methods

class Square(object):
    edge = 5 # meter
    area = 0
    
    def area1(self):
        self.area = self.edge * self.edge
        print("Area: " ,self.area)
    
s1 = Square()
print(s1.edge)
print(s1.area1())

s1.edge = 7
s1.area1()

# %% methods vs functions

class Emp(object):
    age=25
    salary = 1000 #$
    
    #method
    def ageSalaryRatio(self):
        a=(self.age / self.salary)
        print("method: ", a)
        
e1 = Emp()
e1.ageSalaryRatio()

#function    
def ageSalaryRatio(age,salary):
    a=age/salary
    print("function: ",a)
        
ageSalaryRatio(30,3000)

pi = 3.14
r = 5 
area = pi*r**2
print ("function :",a)

#
def findArea (a,b):
    area = a*b**2
    print(area)
    return area

pi = 3.14
r = 5

result1 = findArea(pi,r)
result2 = findArea (pi,10)

print(result1+result2)


# %% initializer or constructor

class Animal(object):
 
    #initializer method
    def __init__(self, name, age):
           self.name = name
           self.age = age
    
    def getAge(self):
        return self.age
    
    def getName(self):
        print(self.name)
    
a1 = Animal("dog", 2)
a2 = Animal("cat", 4)
a3 = Animal("bird", 6)



































