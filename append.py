friends=[]
for f in range(0,4):
    fname=input("my friends name")
    friends.append(fname)
#print(friends)
for name in friends:
    print(name)

d=input("enter name to delete: ")
friends.remove(d)
for name in friends:
    print(name)        

    
