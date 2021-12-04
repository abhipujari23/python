import numpy as np
import matplotlib.pyplot as plt
#Histogram represent the distribution of numerical values
#eg. we could graph the distribution of heights amongst students in class

mu, sigma = 172, 4
#here mu is mean value (average height) and sigma is standard deviation in it


x = mu + sigma * np.random.randn(10000)

plt.hist(x, 100, density=True, facecolor="blue")
#We use hist function to plot histogram
#2nd parameter specifies how many values we want to plot
#we want our values to me normed so we set density to true
#Meaning our y-values will sum up to one and we can view them as percentage
#and we set colour to blue in facecolor

#At this moment the graph is a bit confusing so we will add labels

plt.xlabel("Height")
plt.ylabel("Probability") #here we set label for two axis
plt.title("Height of Students") #here we set the title for the histogram
plt.text(160, 0.125, "172, 4") #This is the text we want to display on graph
plt.axis([155, 190, 0, 0.15]) #here we set range for axis [150, 190] range for X and other range for Y
plt.grid(True)

plt.show()
