import numpy as np
import matplotlib.pyplot as plt
#instead of plotting into subplots we can plot into multiple windows as I mentioned in title :P
#in matplotlib we call these figures

x = np.linspace(0, 5, 200)
y1 = np.sin(x)
y2 = np.sqrt(x)

#Here .figure creates new window for plotting, if we want we can have multiple plotting in one window and single on other
plt.figure(1)
plt.plot(x, y1, 'r-')

plt.figure(2)
plt.plot(x, y2, 'g--')

plt.show()

#By doing this we can show two windows with their graphs at the same time


#FOR STYLING ONLY
#Matplotlib offers different plotting style to choose from.
#If you are interested and want to know how they look when they are applied
#you can see an overview by visiting below link
# https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html

#In order to use a style we need to import the style module of matplotlib then call the function 'use'

# from matplotlib import style
# style.use('ggplot')