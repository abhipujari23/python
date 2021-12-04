import numpy as np
#Joining function is used when we combine multiple array into one new array

a = np.array([10, 20, 30])
b = np.array([20, 20, 10])

#np.concatenate(a, b)
print("np.concatenate joins multiple arrays along an existing axis")
print(np.concatenate((a, b)))

#np.stack(a, b)
print("\n np.stack joins multiple arrays along new axis")
print(np.stack((a, b)))

#np.hstack(a, b)
print("\nnp.hstack stacks the array horizontally (column wise)")
print(np.hstack((a, b)))

#np.vstack(a, b)
print("np.vstack stacks the arrays vertically (row wise)")
print(np.vstack((a, b)))