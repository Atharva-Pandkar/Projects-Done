import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from  sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.preprocessing import StandardScaler


dataset = pd.read_csv("/home/atharva/Udemy/ML/drive-download-20201021T172730Z-001/Classification/Data.csv")


x = dataset.iloc[:,:-1]
y = dataset.iloc[:, -1]

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25, random_state=0)

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)
dictionary = {"Logistic Regression ": 0, "K-N Neighbour": 0, "Support Vector Machine": 0, "Kernel SVM": 0, "Naive Bayes": 0, "Decision Tree Classification": 0, "Random Forest Classification": 0}
n=0
def calulate(classifier,name):
    classifier.fit(x_train,y_train)
    ypred = classifier.predict(x_test)
    if n ==2 :
        ypred = ypred.round()
    ypred = ypred.reshape(len(ypred), 1)

    dictionary[name]=accuracy_score(y_test, ypred)

# Logistic Regression
from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression(random_state=0)
calulate(classifier,"Logistic Regression ")

# K-N Neighbour

from sklearn.neighbors import KNeighborsRegressor

classifier = KNeighborsRegressor(n_neighbors=5)
n=2
calulate(classifier,"K-N Neighbour")
n=0
#Support Vector Machine

from  sklearn.svm import SVC

classifier = SVC(kernel="linear",random_state=0)
calulate(classifier,"Support Vector Machine")

# Kernel SVM

from sklearn.svm import SVC

classifier = SVC(kernel="rbf",random_state=0)
calulate(classifier,"Kernel SVM")

# Naive Bayes

from sklearn.naive_bayes import GaussianNB

classifier = GaussianNB()
calulate(classifier,"Naive Bayes")


# Decision Tree Classification

from sklearn.tree import DecisionTreeClassifier

classifier = DecisionTreeClassifier(criterion="entropy",random_state=0)
calulate(classifier,"Decision Tree Classification")

# Random Forest Regression

from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=50,criterion="entropy",random_state=0)
calulate(classifier,"Random Forest Classification")


for s in dictionary:
    print(s,dictionary[s])