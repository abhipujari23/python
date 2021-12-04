import numpy as np
#SPLITTING FUNCTION

#we can split arrays using splitting functions that split arrays intom multiple sub-array

a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
    [100, 110, 120]
])

#np.split(a, x)
print("np.split splits one array into multiple arrays\n")
print(np.split(a, 2)) 
print("\n")
print(np.split(a, 4))
print("\n")

print(np.hsplit(a, 3))
print("\n")

print(np.vsplit(a, 2))