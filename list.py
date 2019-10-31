num=[1,2,3,4,5,6,7,8]
num2=[]
num3=[]
num4=[]
num5=[]
#print one by one
print(num)
for x in num:
    #print(x)
    num2.append(x)
    num3.append(x+2)
    if x%2==0:
        num4.append(x)
    if x%2!=0:
            num5.append(x)    

print(num2)
print(num3)
print(num4)
print(num5)
