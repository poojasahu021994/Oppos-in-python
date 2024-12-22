class Father:
    def f_property(self,f_name,f_bank):
        self.name=f_name
        self.bank=f_bank
        print(f_name)
        print(f_bank)
class Mother:
    def m_property(self,m_name,m_bank):
        self.n=m_name
        self.b=m_name  
        print(m_name)
        print(m_bank) 
class Son(Father,Mother):
        pass

obj=Son()
obj.f_property("govind","SBI")
obj.m_property("radha","ICICI")
print(dir(Son))         