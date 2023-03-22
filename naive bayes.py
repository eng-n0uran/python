# naive bayes algorithem
import numpy as np
import matplotlib.pyplot as mtp
import pandas as pd
# importing dataset
dataset=pd.read_csv('User_Data.csv')
x= dataset.iloc[:,[2,3]].values
y= dataset.iloc[:,4].values
#splitting the dataset into training set and test set
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)
# feature scalling
from sklearn.preprocessing import StandardScaler
sc= StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.fit_transform(x_test)
# fitting naive bayes to the training set
from sklearn.naive_bayes import GaussianNB
classifier=GaussianNB()
classifier.fit(x_train,y_train)
# prediction the test set resultes
y_pred=classifier.predict(x_test)
#making confusion matrix
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test, y_pred)

 




















