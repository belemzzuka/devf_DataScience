mytuple = ("Sofia", "Pipino", "Renato", "Vaquita", "Warita");

print(mytuple[0])
print(type(mytuple));

#update

#hack to update tuple
aux_list = list(mytuple)
aux_list.append("Tito");
aux_list[1] = "Rita";
mytuple = tuple(aux_list)
print(mytuple)