#Not A Number (NaN)
#this is a special value in Numpy.
#We use it as placeholder for empty spaces
#It can be seen as value that indicates something is missing

#Benefit: When importing big data packets into our application, there will be missing data sometimes
#Instead of setting these values to zero or something else we can set them to NaN and then filter these data out

import numpy as np

a = np.array([[10, 20, 30],
            [40, 50, 60],
            [70, 80, 90]])

#Attributes of Array

#a.shape
print("a.shape provides 2 numbers for column and row like this: ")
print(a.shape)

#a.ndim
print("a.ndim returns how many dimensions our array has: ")
print(a.ndim)

#a.size
print("a.size returns the amount of elements an array has: ")
print(a.size)

#a.dtype
print("a.dtype returns the data type of the values in the array")
print(a.dtype)