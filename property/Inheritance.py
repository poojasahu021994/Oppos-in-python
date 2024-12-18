class p:
    def __init__(self,p_name):
        self.x=p_name
    def p_properties(self,home,bank):
        self.h=home
        self.b=bank
class c(p):
    def c_property(self,quali):
        self.q=quali
        print(self.h)
        print(self.b)        
        print(self.q)        
        print(self.x)    
obj=c("pooja")  
obj.p_properties("Bhopal","SBI")    
obj.c_property("B.Tech")     

        