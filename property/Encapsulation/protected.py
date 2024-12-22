class A:
    _x=10
    def _show(self):
        print("from class A")
class B(A):
    pass
print(dir(B))  
# accessble 

class C:
    pass
print(dir(C))
# not accessble 
