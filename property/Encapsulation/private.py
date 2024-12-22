class A:
    __x=10
    def __show(self):
        print("from class A")
class B(A):
    pass
print(dir(B))
class C:
    pass
print(dir(C))