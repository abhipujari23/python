import matplotlib.pyplot as plt
import numpy as np
#Boxplot is used to split data into quartiles
#We do that to get information about the distribution of out values
#here question is: How widely spread is the data in each quartile

mu, sigma = 172, 4

values = np.random.normal(mu, sigma, 200)

plt.boxplot(values)
plt.title("Student's Height")
plt.ylabel("Height")

plt.show()