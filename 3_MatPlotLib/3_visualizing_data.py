#Instead of plotting function we can also visualize values in form of single dots
import numpy as np
import matplotlib.pyplot as plt

numbers = 10 * np.random.random(100)
plt.plot(numbers, 'bo')
plt.show()

#Here we are generating 100 random numbers using random function
#we plot these numbers as blue dots
#this is defined by the second parameter in plot 'bo'
#in this first letter defines colour b= blue, g= green, r= red, y= yellow
#second letter defines shape of point, o- circle, s= square