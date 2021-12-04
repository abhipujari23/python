#Instead of filling array with same values we can sequence of values by specifing the boundries
#for this we use arange and linspace
import numpy as np

a = np.arange(10, 60, 5) #initial value: 10  final value: 60  step size: 5
print(a)

#by using linspace we can also create list from minimum to maximum value
#but instead of specifing the step size we specify the amount of values that we want in our list
#all the values will be divided equally and will have same distance from each other

b = np.linspace(0, 100, 15)
print(b)

