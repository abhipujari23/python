import numpy as np
#As mentioned previously we can save numpy arrays into CSV files which are just comma-separated text files
#for this we use savetxt

a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
    [100, 110, 120]
])

np.savetxt('myarray.csv', a)
#this saves the file with .csv extension
#This format is very useful as it can be ready by other applications

#in order to read this csv file into our script we use the function loadtxt

b = np.loadtxt('myarray.csv')
print(b)