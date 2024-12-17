class A:
    def new(self):
        print("1st mathod") #declaration
    def new1(self):
        self.new()
        print("2nd method") #calling
obj=A()
#obj.new()
obj.new1()            