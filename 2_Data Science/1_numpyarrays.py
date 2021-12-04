import numpy as np

#to create a NumPy array, we just using the respective function array and pass a list to it

a = np.array([10, 20, 30])
b = np.array([1, 77, 2, 3])

#now we can access the values in the same way as we would do it with list
print("Accessing Array Values")
print(a[0])
print(b)

#Multi-Dimensional Array

a = np.array([[10, 20, 30],
            [40, 50, 60]])
print("Accessing multi-dimentional array")
print(a)
print(a[1][2])

#Full Function
print("Accessing full function Array")
a = np.full((3, 5, 4), 7)
print(a)

#Zeros and Ones

a = np.zeros((3,3))
b = np.ones((2, 3, 4, 2))
print("Creating Array with 0's and 1's")
print(a)
print(b)

#Creating Empty and Random Array

a = np.empty((4, 4)) #creates array without initializing the array
b = np.random.random((2, 5)) #While using random function make sure you are writing random two times
                             #because otherwise you are calling the library
print ("Empty Array")
print(a) #Array is filled with gibbrish values, user should initialize with values before use

print("Random Array")
print(b) #prints random array having value between 0 and 1