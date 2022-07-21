myTuple = ("Sofia", "Pipino", "Renato", "Vaquita", "Warita");
myTuple2 = ("Juana", "Pedro", "Luis", "Paola");

print(myTuple[0])
print(type(myTuple));

#update

#hack to update tuple
aux_list = list(myTuple)
aux_list.append("Tito");
aux_list[1] = "Rita";
myTuple = tuple(aux_list)
print(myTuple)

#Joining tuples
join_tuple = myTuple + myTuple2
print(myTuple.count("Juana"))

print(join_tuple)

#this counts how many is for a specific element
print(join_tuple.count("Sofia"))
print(join_tuple.count("Paola"))