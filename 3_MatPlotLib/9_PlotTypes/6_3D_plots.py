#for 3D plotting we will need to import another plotting module
#It is called mpl_toolkits and it is part of the Matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

ax = plt.axes(projection="3d")
#we can only use this parameter then mplot3d is imported

plt.show()