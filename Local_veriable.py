x=50
class Student:
    global x
    x=10  
    def add():
        print(x)
        y=20
        print(y)

    def add1():
        print(x)
obj=Student
obj.add()
obj.add1()
print(x)

#