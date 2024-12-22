class A:
    __x=10
    def __show1(self):
        print("from class A")
class B(A):
    pass
print(dir(B))        
obj=B()
print(obj._A__x)
obj._A__show1()