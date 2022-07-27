import numpy as np

myArray = np.array([[[0, 1, 2, 3], [244, 355, 98, 15]], [[242, 342, 65, 856], [5, 10, 15, 20]]])

print(myArray)
print(myArray.ndim)
print(myArray[0][1])

print(np.sort(myArray[0][1]))

#print(type(myArray))
print(np.__version__)
#print(np.__doc__)