# Polymorphism - çok şekilcilik
# super classtan sub clasa aktarılan metodu sub classta farklı kullanılmasıdır

class Employee: #super class
    
    def __init__(self, salary): 
        self.salary = salary
    
    def raisee(self): 
        self.salary = self.salary + self.salary * 0.1
        print("emp: ",self.salary)

    
class Engineer(Employee):
    
    def __init__(self, salary):
        Employee.__init__(self, salary)
        
    #polymorphism kullanılan method
    def raisee(self): 
        self.salary = self.salary + self.salary * 0.5
        print("ceng:", self.salary)

class EE(Employee): 
    def __init__(self, salary):
        Employee.__init__(self, salary)

    #polymorphism kullanılan method
    def raisee(self): 
        self.salary = self.salary + self.salary * 0.3
        print("ee: ", self.salary)


e1 = Employee(10)
#print("Employee : ", e1.raisee())

c1 = Engineer(10)
#print("Engineer : ", c1.raisee())

ee1 = EE(10)
#print("EE : ", ee1.raisee())

employee_list = [e1, c1, ee1]

for employee in employee_list:
    employee.raisee()


