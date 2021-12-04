import numpy as np

a = np.array([
    [4, 2, 9],
    [8, 3, 2]
])

#manipulating single element in array
a[1][2] = 7

#SHAPE MANIPULATION FUNCTIONS
#This function allows to restructure array without changing values

#a.reshape(x, y)
print("a.reshape returns an array with the same values structured in different shape")
print(a.reshape(3, 2))

#a.flatten()
print("\na.flatten returns a flattened one-dimensional copy of the array")
print(a.flatten())

#a.ravel()
print("\na.ravel does same as flatten but works with the actual array instead of a copy")
print(a.ravel())

#a.transpose()
print("\na.transpose returns an array with same value but swapped dimensions")
print(a.transpose())

#a.swapaxes()
print("\na.swapaxes returns an array with the same values but two swapped axes")
#print(a.swapaxes())

#a.flat
print("\na.flat is not a function but an iterator for the flattened version of the array")
#This used with flatten to use it in loops

for x in a.flat:
    print(x)
print(a.flat[5])