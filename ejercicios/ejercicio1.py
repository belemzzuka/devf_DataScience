#1) Genera un programa que reciba tu nombre y lo imprima letra por letra.
string = input("Dame un string: ")
i=0

while i < len(string):
    print(string[i])
    i += 1