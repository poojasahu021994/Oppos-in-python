class A:
    x=10
    def __init__(self,name):
        self.name=name

    @classmethod
    def show(cls,age):
        cls.age=age

    @staticmethod    
    def display(school):
        print(school)    
