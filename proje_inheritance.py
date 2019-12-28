# inheritance

class WebSide(object):
    "parent class"
    def __init__(self,name,surname):
        print("Webside is created")
        self.name=name
        self.surname=surname
        
    def loginInfo(self):
        print(self.name +" " + self.surname)

class AWebSide(WebSide):
    "child class"
    def __init__(self, name, surname, ids):
#        super().__init__()
        WebSide.__init__(self, name ,surname)
        print("AWebSide webside is created")
        self.ids = ids
    
    def login(self):
        print(self.name +" " + self.surname +" " + self.ids) # name ve surname yoksa parent clasında initilazer edilir
          

class BWebSide(WebSide):
    
    def __init__(self,name, surname,email):
        WebSide.__init__(self,name,surname)
        print("BWebSide webside is created")
        self.email = email
        
    def login(self):
        print(self.name +" " + self.surname +" " + self.email) # name ve surname yoksa parent clasında initilazer edilir
    


p1 = WebSide("name","surname")
p2 = AWebSide("name1","surname1", "123")
p3 = BWebSide("name2", "surname2", "email@")

