#Syntax
myDictionary = { 
    "name" : "Belem",
    "last_name" : "Garrido", 
    "age" : 36,
    "weight" : 58.5,
    'city' : 'Veracruz',
    "hobbies" : [ "skate", "piano", "lego" ]
}

print(myDictionary)

#access to a key
print(myDictionary["weight"])

#class
print(type(myDictionary))

#length dictionary
print(len(myDictionary))

#looping a dictionary
#values
for value in myDictionary.values():
    print(value)

#keys
for key in myDictionary.keys():
    print(key)

#keys and values: items
for key, value in myDictionary.items():
    print(key, value)

#copying a dictionary
myNewDictionary = myDictionary.copy()
print(myNewDictionary)