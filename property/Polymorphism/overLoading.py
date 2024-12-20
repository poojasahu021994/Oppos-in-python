class A:
    def add(self,*n):
        sum=0
        for i in n:
            sum=sum+i
        return sum
obj=A()
x=obj.add(10,20)
print(x)
y=obj.add(10,20,30)
print(y)    