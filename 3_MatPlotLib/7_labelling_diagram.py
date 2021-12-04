import numpy as np
import matplotlib.pyplot as plt
#In order to make graph more understandable we need labels
#we should label the axes, we should give window titles and in some cases we should also add a legend

#Setting Titles
#lets set title to our plotting window

x = np.linspace(0, 50, 100)
y = np.sin(x)

plt.title("Sine Function Plot") #This creates main title for our plotting window
plt.suptitle("Data Science") #This adds additional title nentered about the title

plt.grid(True) #Using this value we turn on grid for our plot

#labelling axes
# these will create X and Y axis labels
plt.xlabel("x_values")
plt.ylabel("y_values")

plt.plot(x, y)
plt.show()