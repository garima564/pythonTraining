student={"name":"shiva","age":22,"class":"12th"}
print(student["age"])
print(student.get("class"))
student["name"]="shivshankar"
print(student["name"])
student["mobile"]="9839261780"
print("...................")
for x in student:
    print(x)
    #print(student[x])
print("------------------") 
for x in student.values():
    print(x)   
print("**********************") 
for x,y in student.items():
    print(x,y)   
