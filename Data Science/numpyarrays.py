import numpy as np

#to create a NumPy array, we just using the respective function array and pass a list to it

a = np.array([10, 20, 30])
b = np.array([1, 77, 2, 3])

#now we can access the values in the same way as we would do it with list

print(a[0])
print(b)

#Multi-Dimensional Array

a = np.array([[10, 20, 30],
            [40, 50, 60]])

print(a)
print(a[1][2])

#Full Function
a = np.full((3, 5, 4), 7)
print(a)

#Zeros and Ones

a = np.zeros((3,3))
b = np.ones((2, 3, 4, 2))

print(a)
print(b)