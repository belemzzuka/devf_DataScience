myList = [ 1, 2, 3, 4, 5, 6, 7, 8 ];

myList.append(9);
myList.append(10);
myList.insert(0,0); # Insertar en la posición 0, un 0

# Eliminar elementos de una lista
myList.remove(7); # Remover el elemento, no la posicion. Compara el valor y si existe ese valor lo remueve
myList.pop(); # Elimina el último elemento de la lista
myList.pop(1); # Elimina el elemento que le indicas
del myList[2]; # Elimina el elemento en la posición que le indicas
# myList.clear(); # Borra todos los elementos de la lista. La deja en blanco.

# Looping a list - METHOD 1
print("FOR IN LOOP");
for x in myList:
    print(x)

# Looping a list - METHOD 2
print("FOR IN RANGE LOOP")
for i in range(len(myList)):
    print(myList[i]);

# Looping a list - METHOD 3
print("WHILE LOOP");
iterator = 0;
while iterator < len(myList):
    print(myList[iterator]);
    iterator = iterator + 1;

# Print the list
print(myList);

# Looping a list - METHOD 4
print("LOOPING LIST BY COMPREHENSION LIST");
[print(x) for x in myList]

import time
start_time = time.time()
# main()
print("--- %s seconds ---" % (time.time() - start_time))