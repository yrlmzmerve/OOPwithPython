#RENT VEHICLE PROJECT
import datetime

class VehicleRent(): #parent class
    
    def __init__(self,stock):
        self.stock = stock #araç sayısı
        self.now = 0 # aracın kiralanmaya başladıgı zamanı tutmak için
    
    def displayStock(self):
        
        print("{} vehicle available to rent".format(self.stock))
        return (self.stock)
    
    def rentHourly(self, n):
        """
            rent hourly
        """
        if n <= 0:
            print("Number should be positive")
            return None
        elif n > self.stock:
            print("Sorry, {} vehicle available to rent".format(self.stock))
            return None
        else:
            self.now = datetime.datetime.now()
            print("Rented a {} vehicle for hourly at {} hours".format(n,self.now.hour))
            self.stock = self.stock-n
            
            return self.now
            
    def rentDaily(self, n):
        
         # n is number of vehicle
        if n < 0:
            print("Number should be positive")
            return None
        
        elif n > self.stock:
            print("Sorry {} vehicle available to rent".format(self.stock))
            return None
        
        else:
            self.now = datetime.datetime.now()
            print("Rented a {} vehicle for hourly at {} hours".format(n,self.now.hour))
            self.stock = self.stock-n
            
            return self.now
            """pc zamanından zamanı almak
            #(2019, 12, 29, 13, 11, 39, 268699) formatında gelir
            #self.now.hour -> saati alabilirz
            #return noww : saat farkına göre fatura cıkartmak ıcın
            """
    
    def returnVehicle(self, request, brand):
        " return a bill "
        car_h_price = 10
        car_d_price = car_h_price *8/10*24
        bike_h_price = 10
        bike_d_price = bike_h_price*7/10*24
        
        """
        request = 
            rentalTime - araç ne zaman kiralandı
            rentalBasis - ne kadar süreyle kiralandı - günlük ya da saatlik
            numOfVehicle - kiralanan araç sayısı
            
        brand = car or bike
        """
        
        rentalTime, rentalBasis, numOfVehicle = request
        bill = 0
        
        if brand =="car":
            if rentalTime and rentalBasis and numOfVehicle: #bunlar boş değilse
                self.stock += numOfVehicle
                now = datetime.datetime.now() # self.now ile now farklı bu local variable
                rentalPeriod = now - rentalTime #aracın kiralandıgı zaman- iade ettiği zaman
                
                if rentalBasis == 1: # hourly
                    bill = rentalPeriod.seconds/3600*car_h_price*numOfVehicle
                
                elif rentalBasis == 2: # daily
                    bill = rentalPeriod.seconds/(3600*24)*car_d_price*numOfVehicle
                    
                if (2 <= numOfVehicle):
                    print("You have extra 20% discount")
                    bill = bill*0.8
                
                print("Thank you for returning your car")
                print("Price: $ {}".format(bill))
                return bill
            
        elif brand == "bike":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime 
                
                if rentalBasis == 1: # hourly
                    bill = rentalPeriod.seconds/3600*bike_h_price*numOfVehicle
                
                elif rentalBasis == 2: # daily
                    bill = rentalPeriod.seconds/(3600*24)*bike_d_price*numOfVehicle
                    
                if (4 <= numOfVehicle):
                    print("You have extra 20% discount")
                    bill = bill*0.8
                
                print("Thank you for returning your bike")
                print("Price: $ {}".format(bill))
                return bill
        else:
            print("You do not rent a vehicle")
            return None
              
        
class CarRent(VehicleRent): #Child class
    
    global discount_rate
    discount_rate=15
    
    def __init__(self,stock):
        VehicleRent.__init__(self,stock)
    
    def discount(self, b):
        bill = b - (b*discount_rate)/100
    
class BikeRent(VehicleRent): #Child class
    
    def __init__(self,stock):
        VehicleRent.__init__(self,stock)
        
class Customer():
        
     def __init__(self):
        self.bikes = 0 #kiralanan bike sayısı
        self.rentalBasis_b = 0 # bike için saatlik mi günlük mü kiralandıgını
        self.rentalTime_b=0 #hangi saatte kiraladıgı
        
        self.cars = 0 # kiralanan araç sayısı
        self.rentalBasis_c = 0 # car için saatlik mi günlük mü kiralandıgını
        self.rentalTime_c = 0 #hangi saatte kiraladıgı

     def requestVehicle(self, brand):
        """
            take a request bike or car from customer
        """
        if brand == "bike":
            bikes = input("How many bikes would you like to rent?")
            
            try:
                bikes = int(bikes)
            except ValueError:
                print("Number should be Number")
                return -1
            
            if bikes < 1:
                print("Number of Bikes should be greater than zero")
                return -1
            else:
                self.bikes = bikes
            return self.bikes
            
        elif brand =="car":
            
            cars = input("how many car would you like to rent?")
            try:
                cars = int(cars)
            except ValueError:
                print("Number should be Number")
                return -1
            
            if cars < 1 :
                print("Number of cars should be greater then 0")
                return -1
            
            else:
                self.cars = cars
            return self.cars
        
        else:
            print("Request vehicle error")
                
    
     def returnVehicle(self, brand):
        """
            return bikes or cars
        """
        if brand == "bike":
            if self.rentalTime_b and self.rentalBasis_b and self.bikes:
                return self.rentalTime_b, self.rentalBasis_b,  self.bikes
            else:
                return 0,0,0
        elif brand == "car": 
            if self.rentalTime_c and self.rentalBasis_c and self.cars:
                return self.rentalTime_c, self.rentalBasis_c,  self.cars
            else:
                return 0,0,0
        else:
            print("Return vehicle Error")



























