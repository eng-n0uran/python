#nouran E
import numpy as np
import pandas as pd
#importing the dataset
dataset = pd.read_csv('iris.csv')
x = dataset.iloc[:, 0:4].values
y = dataset.iloc[:,4].values
#splitting the dataset into the training set and test set
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)
#feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)
#Performing LDA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
lda =LDA(n_components=1)
x_train = lda.fit_transform(x_train,y_train)
x_test = lda.transform(x_test)
#training and making prediction using naiva bayes
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(x_train,y_train)
#predicting the test set results
y_pred = classifier.predict(x_test)
print(y_pred,y_test)
#making the confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
print(cm)
#accuracy
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,y_pred)*100)
print("####################################################")
##########
#training and making prediction using SVM
from sklearn.svm import SVC # "support vector classifier"
classif = SVC(kernel='linear',random_state=0)
classif.fit(x_train,y_train)
#predicting the test set results
y_pre = classif.predict(x_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,y_pre)*100)
print("####################################################")
#Random forest classifier
from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(max_depth=2, random_state=0)

classifier.fit(x_train, y_train)
y_pred= classifier.predict(x_test)

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

cm =confusion_matrix(y_test, y_pred)
print(cm)
print('Accuracy' + str(accuracy_score (y_test, y_pred)))

print("####################################################")
##########
#without LDA
# Training and Making Predictions using Naive Bayes

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)

#Making the Confusion Matrix

from sklearn.metrics import confusion_matrix
cm =confusion_matrix(y_test, y_pred)
print(cm)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,y_pred)*100)

#Training and Making Predictions using SVM

from sklearn.svm import SVC # "Support vector classifier"
classif = SVC (kernel="linear", random_state=0)

classif.fit(x_train, y_train)
y_pre = classif.predict(x_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,y_pre)*100)





















