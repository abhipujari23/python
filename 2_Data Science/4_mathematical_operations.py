# Arithmatic Operations
import numpy as np

a = np.array([
    [1, 4, 2],
    [8, 8, 2]
])

#Different arithmatic operations on Array :: operation is applied to all the elements in array

#Addition
print("\nAddition")
print(a + 2)

#Substraction
print("\nSubstraction")
print(a - 2)

#Multiplication
print("\nMultiplication")
print(a * 2)

#Division
print("\nDivision")
print(a / 2)

#Mathematical Function

#We can apply mathematical function to each value in  array

#np.exp(a)
print("\n\nnp.exp function takes e to the power of each element in array")
print(np.exp(a))

#np.sin(a)
print("\nnp.sin returns sine value of each element in array")
print(np.sin(a))

#np.cos(a)
print("\nnp.cos returns cosine value of each element in array")
print(np.cos(a))

#np.tan(a)
print("\nnp.tan returns tangent value of each element in array")
print(np.tan(a))

#np.log(a)
print("\nnp.log returns logarithm value of each element in array")
print(np.log(a))

#np.sqrt(a)
print("\nnp.sqrt returns square root value of each element in array")
print(np.sqrt(a))

#AGGREGATE FUNCTIONS
# now lets get into statistics, using numpy we can get a key statistic from all out values

#a.sum()
print("\n\na.sum returns sum of all the elements in the array")
print(a.sum())

#a.min()
print("\na.min returns lowest of all the elements in the array")
print(a.min())

#a.max()
print("\na.max returns highest of all the elements in the array")
print(a.max())

#a.mean()
print("\na.mean returns the arithmatic mean of all the elements in the array")
print(a.mean())

#np.median()
print("\nnp.median returns median of all the elements in the array")
print(np.median(a))

#np.std()
print("\n\nnp.std returns the standard deviation of all the elements in the array")
print(np.std(a))
