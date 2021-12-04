import numpy as np
import matplotlib.pyplot as plt
#Our plots are not limited to single graph
#we can plot multiple graphs in different colour and shapes as mentioned previously

x = np.linspace(0, 5, 200)

y1 = 2 * x
y2 = x ** 2
y3 = np.log(x)

plt.plot(y1)
plt.plot(y2)
plt.plot(y3)
#here we plot all the points and then use show function resulting in all 3 showing in plotting window

plt.show()