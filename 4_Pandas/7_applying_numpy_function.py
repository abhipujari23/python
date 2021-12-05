#instead of using builtin Pandas function we can also use methods we know
#For this we just need to use apply function of the data frame and pass our method
from repeat import dfInfo as df
import numpy as np

print(df['Age'].apply(np.sin))
#Here we apply sine function to our age column, It is not required but it shows how this works