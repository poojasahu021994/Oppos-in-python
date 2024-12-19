# Single lavel inhertance
class P:
    def __init__(self,p_name):
        self.x=p_name
    def p_properties(self,home,bank):
        self.h=home
        self.b=bank
class C(P):
    def c_property(self,quali):
        self.q=quali
        print(self.h)
        print(self.b)        
        print(self.q)        
        print(self.x)    
obj=C("pooja")  
obj.p_properties("Bhopal","SBI")    
obj.c_property("B.Tech")     

class P:
    def __init__(self,p_name):
        self.x=p_name
    def p_properties(self,home,bank):
        self.h=home
        self.b=bank
        print(self.h)
        print(self.b) 
class C(P):
    def c_property(self,quali):
        self.q=quali
        self.p_properties("bhopal","icici")      
        print(self.q)        
        print(self.x)    
obj=C("pooja")  
# obj.p_properties("Bhopal","SBI")    
obj.c_property("B.Tech")
