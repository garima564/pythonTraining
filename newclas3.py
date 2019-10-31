class StringCheck:
    def printlast(self,word):
        l=len(word)
        if l>=2:
            print(word[-1])
        else:
            print("word is to small")

     

            
#y=StringCheck()            
#y.printlast("kavi")
class B(StringCheck):
    pass
y=B()    
y.printlast("shiv")