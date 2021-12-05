#In contrast to series, Pandas is multidimensional and looks like table
#You can image it to be like Excel table or database table
import pandas as pd

data = {'Name': ['Anna', 'Bob', 'charles'],
        'Age': [24, 32, 35],
        'Height': [176, 187, 175]}

df = pd.DataFrame(data)
#Here we first create a dictionary with some data and we feed the data into our dataframe
#then it looks like:
print(df)

#Without any manual work, we already have structured dataframe and table

#To access the value however is a bit complicated that series
#we need to specify two values
print(df['Name'][1])

#This is useful when we want to save specific column of data into new one
#we can also choose multiple columns
print(df[['Name', 'Height']])