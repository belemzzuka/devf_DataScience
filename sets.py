mySet = { "Tesla", "Ferrari", "BMW", "Aston Martin", "Tesla" }
mySet2 = { "Chevrolet", "Nissan", "Kia" }

for element in mySet:
    print(element)

mySet.add("ADD")
mySet.add("BMW")
mySet.update(mySet2)

print(mySet)
print(type(mySet))