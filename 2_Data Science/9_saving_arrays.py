import numpy as np
# In order to save arrays we can use integrated numpy format or CSV-format

#NUMPY FORMAT
#basically we are serializing tje objects so that we can use it later this is done by using save function

a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
    [100, 110, 120]
])

np.save('myarray', a)

#This creates a file "myarray.npy" in the main(root) directory