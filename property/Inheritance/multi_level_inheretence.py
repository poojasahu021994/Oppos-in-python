# Multi level inheretance
class GrandP:
    def g_properties(self,car):
        self.g=car
        print(self.g)
class P(GrandP):
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
obj.g_properties("i20")
obj.c_property("B.Tech")


# Example 2 (multi level inheritance)

class Gf:
    def name(self,name):
        self.x=name
        print(self.x)
class F(Gf):
    def f_name(self,f_name):
        self.y=f_name
class C(F):
    def c_name(self,c_name):
        self.z=c_name
        print(self.z)
obj=C()
obj.name("pooja") 
obj.c_name("gourik")             
        