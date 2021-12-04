import matplotlib.pyplot as plt
import numpy as np
#In order to plot a function with surface we need to calculate every point on it which is impossible
#That is why we calculate enough to estimate the graph
#In this case X and Y will be inputs and Z-function will be the 3D-result which is composed of them

ax = plt.axes(projection = '3d')

def z_function(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)

#we start by defining z_function which is a combination of sine, squareroot and squaring the input
#Our inputs are just 50 numbers from -5 to 5

X, Y = np.meshgrid(x, y)
Z = z_function(X, Y)

ax.plot_surface(X, Y, Z)

plt.show()