import numpy as np
import matplotlib.pyplot as plt

#Sometimes we have multiple graphs and objects in a plot
#There we use Legends to label individual elements in order to make it more readable

x = np.linspace(10, 50, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.log(x/3)

plt.plot(x, y1, 'b-', label="Sine")
plt.plot(x, y2, 'g-', label="Cosine")
plt.plot(x, y3, 'r-', label="Logarithm")

plt.legend(loc='upper left')

plt.show()

#now that we know about plotting and graphing, here's how to save it

plt.savefig("function.png")