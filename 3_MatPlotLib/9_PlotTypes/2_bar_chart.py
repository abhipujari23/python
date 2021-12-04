import numpy as np
import matplotlib.pyplot as plt

#The easiest way to see any information is bar chart

#here we will plot the skill level of three people in IT relm

bob = (90, 67, 87, 76)
charles = (80, 80, 47, 66)
daniel = (40, 95, 76, 89)

skills = ("Python", "Java", "Networking", "Machine Learning")

width= 0.2
index = np.arange(4)
#here we define an array with indices one to four and a bar width of 0.2

plt.bar(index, bob, width=width, label = "Bob")

plt.bar(index + width, charles, width = width, label = "Charles")

plt.bar(index + width*2, daniel, width = width, label = "Daniel")


plt.xticks(index + width, skills)
plt.ylim(0, 120)

plt.title("IT Skill Levels")
plt.xlabel("Skills")
plt.ylabel("Skill Level")

plt.legend()

plt.show()