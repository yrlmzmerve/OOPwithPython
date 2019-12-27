#Calculator Project

class Calculator (object):
    "calculator"
    
    #init method
    def __init__ (self, a, b):
        "initialize values"
        #attiribute
        self.value1 = a
        self.value2 = b
        
    def add(self):
          "addition a+b = result -> return result"
          return self.value1 + self.value2   
         
    def multiply (self):
        "multiplication a * b = result -> return result"
        return self.value1 * self.value2 
    
    def subtraction (self):
        "subttraction a - b = result-> return result"
        return self.value1 - self.value2
    
    def division(self):
        "division a/b = result -> return result"
        return self.value1 / self.value2
        
print("Choose add(1), multiply(2), subtraction(3), division(4)")
selection = input ("Select 1, 2, 3 or 4 :")

v1 = int(input("First value: "))
v2 = int(input ("Second value : "))

c1 = Calculator(v1,v2)
if selection == "1":
    add_v= c1.add()
    print("Add: {}" .format(add_v))
elif selection == "2":
    mult_v = c1.multiply()
    print("Mult {}" .format(mult_v))
elif selection =="3":
    subt_v = c1.subtraction()
    print("Subt {}".format(subt_v))
elif selection =="4":
    div_v = c1.division()
    print("Div {}".format(div_v))
else:
    print("There is no selection")

        
print()














