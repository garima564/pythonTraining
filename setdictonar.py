fruits={"apple","banana","orange","apple"}
print(fruits)
for x in fruits:
    print(x)
    print("........")
    print("mango" in fruits)
#add more data in set
fruits.add("cherry")    
print(fruits)
#add multiple data on set
fruits.update(["kiwi","guavava"])
print(fruits)
#delete data in set
fruits.remove("apple")
print(fruits)
#remove will give error if data is not found 
fruits.discard("orange")
print(fruits)
fruits.discard("garima")
fruits.pop()
print(fruits)
fruits.clear()
print(fruits)
del fruits


