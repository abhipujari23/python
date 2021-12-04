# now we will create our own function to plot the graph
import numpy as np
import matplotlib.pyplot as plt

x_values = np.linspace(0, 10, 100)
y_values = (6 * x_values - 30)**2

plt.plot(x_values, y_values)
plt.show()