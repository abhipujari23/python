import numpy as np
import matplotlib.pyplot as plt
#sometimes we want to draw multiple graphs but not want them to be in same plot
#For that we have subplots, these are showin in the same window but independent from each other

x = np.linspace(0, 5, 200)
y1 = np.sin(x)
y2 = np.sqrt(x)

plt.subplot(211)
plt.plot(x, y1, 'r-') #here we specify x and y values and 'r-' is used to format the line
#r specifies colour as previous lesson and - specifies solid line
plt.subplot(212)
plt.plot(x, y2, 'g--') #here -- specifies broken line
# here we pass x and y values, first defines number of rows and 2nd defines the number of columns
plt.show()