from repeat import df

#for dataframes we have a couple of basic functions and attributes that we already know from lists and numpy
#for below examples df is the dataframe name we created in 4_pandas_data_frame.py and it has been imported in this file by repeat.py

#df.T
# df.T transposes the rows and columns of the dataframe
#print(df) #uncomment this to compare
print(df.T)

print("\nData Type:")
#df.dtypes
# df.dtypes returns the data types of the data frame
print(df.dtypes)

print("\nDimension of dataframe:")
#df.ndim
# df.ndimm returns the dimentsions of the dataframe
print(df.ndim)

print("\nShape of Dataframe:")
#df.Shape
# df.shape returns the shape of the dataframe
print(df.shape)

print("\nSize of Dataframe:")
#df.size
# df.size returns the number of elements in the dataframe
print(df.size)

print("\nHead of dataframe:")
#df.head(n)
#df.head returns the first n rows of the dataframe
print(df.head(1))

print("\nTail of dataframe:")
#df.tail(n)
#df.tail returns the last n rows of the dataframe
print(df.tail(1))