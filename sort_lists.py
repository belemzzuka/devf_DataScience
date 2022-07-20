def helper(number):
    return abs(number - 10) #Esta funcion que definimos es para ordenarlos conforme estén mas cerca del numero 10

countries = [ "Mexico", "Estados Unidos", "Canada", "Polonia", "canada", "brasil" ];
countries.sort();
countries.sort( key = str.islower, reverse = True ); # Ordena primero los que empiezan con minusculas y luego los de mayusculas

numbers = [ 3, 55, 215, 104, -344, -2]
numbers.sort(reverse = True)
numbers.sort( key = helper ) #Defines una funcion para ordenar los numeros

print(countries);
print(numbers);