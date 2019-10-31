class Student:
    def __init__(self,name,roll,contact):
        self.name=name.upper()
        self.roll=roll
        self.contact=contact
    def hello(self):
        print("my firts class method")
    def printlast(self,word):
        l=len(word)
        if l>=2:
            print(word[-1])
        else:
            print("word is to small")
         


        
p1=Student("john",136,9839261780)
p1.hello()

print(p1.name)
print(p1.roll) 
print(p1.contact)
p2=Student("garima",145,78890999)
print(p2.name)
print(p2.roll)
print(p2.contact)
p1.printlast("India")