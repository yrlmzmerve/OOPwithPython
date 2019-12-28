#Encapsulation

#Method ya da variable'ların erişiminin kısıtlanması
# __ ile private yapılır

class BankAccount(object):
    
    def __init__(self,name, money, job):
        self.name = name #global
        self.__money = money #private
        self.job = job
    
    #get and set global
    
    def getMoney(self):
        return self.__money
    
    def setMoney(self, amount):
        self.__money = amount
    
    #private
    def __increase(self):
        self.__money = self.__money + 500
        
p1 = BankAccount("Merve", 7000, "Engineer")
p2 = BankAccount("Berra", 5000, "Banker")

print("get method: ", p1.getMoney())
p1.setMoney(9500)
print("after set method: ", p1.getMoney())

#p1.__increase()
#print("after raise: ", p1.getMoney())