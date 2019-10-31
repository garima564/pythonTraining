#wap to print 10 languages name using list
#step1.intialize the list
lang1=[]
for l in range(0,5):
    tlang=input("enter language name: ")
    lang1.append(tlang)
for lname in lang1:
    print(lname.upper()) 

    l=len(lname)
    print("there are",l,"char.")