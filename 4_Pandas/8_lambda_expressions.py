#Python has very powerful exxpression known as lambda expression
#They can be thought as nameless functions that we pass as parameters
from repeat import dfInfo as df

print(df['Age'].apply(lambda x: x * 100))
#by using the keyword lambda we create a temporary variable that represents the individual values
#after colon we define what we want to do. In this case we multiply all the values of the column 'Age' by 100

dfl = df[['Age', 'Height']]  
print(dfl.apply(lambda x: x.max() - x.min()))
#This gives us the output stating: The oldest and youngest are 33 years apart
#and the tallest and shortest are 24 centimeters apart