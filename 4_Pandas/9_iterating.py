from repeat import dfInfo as df
#Iterating over dataframes is quiet easy with Pandas
#We can either do it the classis way or use specific function to do it

for x in df['Age']:
    print(x)
print("\n")
#as you can see iterating over column value is very simple and nothing new
#few important functions iteritems(), iterrows(), itertuples()

#lets looks at practical example

for key, value in df.iteritems():
    print("{}: {}".format(key, value)) #this provides output of all rows for each column

#on the other hand when we use iterrows() we can print out all the column values for each row or index

for index, value in df.iterrows():
    print("{}: {}\n".format(index, value))