#2) Genera un programa que imprima las tablas de multiplicar.

num = input("Dame el número a multiplicar: ")

for x in range(1,11):
    #product = int(num) * x
    #print(int(num), "x", x, "=", product)
	print(f'{int(num)} x {x} =  {int(num) * x}')