# we will need to import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression # This is used to create, train and use our regression model
from sklearn.model_selection import train_test_split #we will use this to prepare and split data

#first we load data from csv file into Pandas Dataframe
data = pd.read_csv('student-mat.csv', sep=';')

data = data[['age', 'sex', 'studytime', 'absences', 'G1', 'G2', 'G3']]
#Column G1, G2, G3 are three grades that the student gets
#Our goal is to predict the third and final grade by looking at the other values like first grade , age, sex and so on

#Here we have a small problem, Sex feature is not numeric but stored as F(Female) or M(Male)
#But for us to work and register it in the coordinate system we have to convert it into numbers
# so we use

data['sex'] = data['sex'].map({'F': 0, 'M': 1})
#we use map function to do this, this changes F to 0 and M to to 1 in Sex column so we can work with it

#and Fianlly we define column of desired label as a variable to make it easier to work with
prediction = 'G3'

######################

### Preparing Data ###
######################

#Our data is loaded and selected but in order to train and test it we have to reformat them
# sklearn models do not accept Pandas data frame but only Numpy arrays
# And that is why we turn our features into an x-array and our labels into y-array

X = np.array(data.drop([prediction], 1))
Y = np.array(data[prediction])

#Np.array converts columns into array and drop function returns the data frame without the specified column
#X array now contains all of our columns except for final grade
#Final Grades are stored in Y array


#In order to train and test the model we have to split our availabel data
# First part is used to get the hyperplanes to fit our data
# Second part is used to check the accuracy of the prediction, with previously unknown data

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1)
#here we divide X and Y arrays into 4 arrays
#the test_size parameter specifies what percentage of record should be used for testing
#here we use 10%, this is the recommended value

############################

### Training and Testing ###
############################

#Now we can start training and testing our model, for that we first define our model.

model = LinearRegression()
model.fit(X_train, Y_train)

#By using the constructor of the LinearRegression class, we create our model
# we then use the fit function and pass our training data
# Now our model is already trained and it has now adjusted its hyperplane sothat it fits all of our values
# 
# In order to test how well our model performs we cna use the score method and pass our testing data

accuracy = model.score(X_test, Y_test)
print(accuracy)