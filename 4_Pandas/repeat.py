import pandas as pd

#Used to series lessons
series = pd.Series([10, 20, 30, 40],['A','B','C','D'])


#used for DataFrame Lessons
data = {'Name': ['Anna', 'Bob', 'charles'],
        'Age': [24, 32, 35],
        'Height': [176, 187, 175]}

df = pd.DataFrame(data)


#used for Statistical lessons
data = {'Name': ['Anna', 'Bob', 'charles', 'Daniel', 'Evan', 'Fiona', 'Gerald', 'Henry', 'India'],
        'Age': [24, 32, 35, 45, 22, 54, 55, 43, 25],
        'Height': [176, 187, 175, 182, 176, 189, 165, 187, 167]}

dfInfo = pd.DataFrame(data)