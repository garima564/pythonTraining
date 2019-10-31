class Car:
    def __init__(self,name):
        self.name=name
    def myname(self):
        print(self.name)

class Bmw(Car):
    def __init__(self,name):
        super().__init__(name)
        self.myname=name
        
    def myname1(self):
        print("from child",self.myname)
    

y=Bmw("x11")
y.myname()
y.myname1()

