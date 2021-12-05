#Python has very powerful exxpression known as lambda expression
#They can be thought as nameless functions that we pass as parameters
from repeat import dfInfo as df

print(df['Age'].apply(lambda x: x * 100))