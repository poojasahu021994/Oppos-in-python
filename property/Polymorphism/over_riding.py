class A:
    def display(self):
        print("from dose A")

class B(A):
    def display(self):
        print("from class B")    
    def p_display(self):
        self.display()
        super().display()

obj=B()
obj.p_display()
obj.display()       