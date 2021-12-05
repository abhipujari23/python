#Pandas provies high-performance tools for data amnipulation and analysis.
#It is ver effecient at converting data formats and querying data out of databases
#Two main data structure of Pandas are 'series' and 'dataframe'
#To work with Pandas we need to import the module
import pandas as pd

#Series in Pandas is One-Dimentional Array which is labeled. It is data science equivalent of an ordinary python dictionary

series = pd.Series([10, 20, 30, 40],['A','B','C','D'])
#here first parameters is full of values(here numbers) and second parameter is the list of indices or keys(here letters)
#When we print our series we can see what structure looks like

print(series)
#In output first column represents indices and second column represents values

#Note: from next lessons I have used repeat.py as custom import for importing pandas and series 