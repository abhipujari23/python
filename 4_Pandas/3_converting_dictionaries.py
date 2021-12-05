#Since series and dictionaries are quire similar, we can easily convert our python dictionary into Pandas series
import pandas as pd

myDict = {'A': 10, 'B': 20, 'C': 30}

series = pd.Series(myDict)
#now keys are our indices and values remain values
# we can also change the order of the indices
# series  = pd.Series(myDict, index['C','A','B'])