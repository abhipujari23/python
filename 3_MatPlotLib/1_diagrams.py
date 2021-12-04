#Visualizing our data is crucial for data science
#helps to analyze data and make predictions
# we use matplotlib library for plotting and visualizing data

#modules needed numpy and matplotlib.pyplot for plotting
import numpy as np
import matplotlib.pyplot as plt

# in order to plot a function we need x-values(input) and y-values(output)
x_values = np.linspace(0, 20, 100)

y_values = np.sin(x_values)
#function gets applied to every item of the input array

#to plot we do
plt.plot(x_values, y_values)
#now plotting is completed and we need to display it, we use
plt.show()