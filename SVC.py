import pandas as pd
data_set=pd.read_csv( 'C:/Users/TC/Desktop/FCI/all sections need/sections level 3/python/User_Data.csv ')
print(data_set.head())
#extracting independant and dependant variables
x= data_set.iloc[:,[2,3]].values
y= data_set.iloc[:,4].values
#splitting dataset inton training and test data
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)
# feature scalling
from sklearn.preprocessing import StandardScaler
st_x= StandardScaler()
x_train=st_x.fit_transform(x_train)
x_test=st_x.fit_transform(x_test)
from sklearn.svm import SVC # suppot vector classifier
classifier=SVC(kernal='linear',random_state=0)
classifier.fit(x_train,y_train)
# predicting the test set result
y_pred=classifier.predict(x_test)
print(y_pred)
#creating the confusion matrix
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test, y_pred)
print(cm)



