import matplotlib.pyplot as plt
#Pie charts are used to display proportions of numbers
#Here we could graph how many percentage of the students have which nationality

labels = ('American', 'German', 'French', 'other')
values = (47, 23, 20, 10)

#Here we have two tuples with nationality and percentages
#we plot pie chart by

plt.pie(values, labels = labels, autopct="%.2f%%", shadow=True)
plt.title("Student Nationality")

plt.show()