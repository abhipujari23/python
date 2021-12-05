from repeat import dfInfo as df
#For statistics we have extended our data frame and added more information in repeat.py

#count()
#Count the numbers of non null elements
print("Total Count:")
print(df.count())

#sum()
#sum returns the sum of values of the selected column
#Here we use age column for demostration
print("\nSum of Age:")
print(df['Age'].sum())

#mean()
#mean returns the arithmatic mena of values of the selected column
#Here we use age column for demostration
print("\nMean of Age:")
print(df['Age'].mean())

#median()
#median returns the median of values of the selected column
#Here we use Height column for demostration
print("\nMedian of Height:")
print(df['Age'].median())

#sum()
#sum returns the sum of values of the selected column
#Here we use age column for demostration
print("\nSum of Age:")
print(df['Age'].sum())
