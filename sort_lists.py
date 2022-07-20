def helper(number):
    return abs(number - 10) #Esta funcion que definimos es para ordenarlos conforme estén mas cerca del numero 10

countries = [ "MX", "US", "CAN", "POL" ];
numbers = [3,55,215,104,-344, -2]

countries.sort();
numbers.sort(reverse = True)
numbers.sort(key=helper) #Defines una funcion para ordenar los numeros

print(countries);
print(numbers);