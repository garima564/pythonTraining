cname=" "
mediname={'ajubi':5,'crocin':6,'saredon':7,'m16':9}
qty=0

cname=input("enter customer name:")
xname=input("enter medicine name:")
if xname in mediname:
    qty=int(input("enter qty:"))
    #print(mediname[xname])
    p=mediname[xname]
    t=p*qty
    print(t)
else:
    print("medi is out of stock:")
print("..................................")
print("NAME",xname)
print("**********************************")
print("medicine name      rate     qty    total")         
print("???????????????????????????????????????")
print(" ",xname,"          ",mediname[xname],"      ",qty,"    ",t)