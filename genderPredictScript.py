from sklearn import tree
from sklearn import neighbors
from sklearn import gaussian_process

#[height, weight, shoe size]
X = [[181,80,10],[161,70,6],[171,66,7],[176,88,7],[189,100,8],[141,80,5],[156,78,6],[161,50,6],[171,60,7],[151,78,7],[171,40,7]]
#Gender
Y = ['male','male','male','male','male','female','female','female','female','female','female']

#Define 'DecisionTreeClassifier' Classifier From the imported Tree
decisionTreeclassifier = tree.DecisionTreeClassifier()

#Fit the data into the Classifier
decisionTreeclassifier = decisionTreeclassifier.fit(X,Y)

#Perform Prediction
decisionTreeclassifierPrediction = decisionTreeclassifier.predict([[161,60,9]])

#Print the Classifier
print(decisionTreeclassifier)

#Print the Prediction
print(decisionTreeclassifierPrediction)



#Define 'KNeighborsClassifier' Classifier From the imported Tree
kNeighborsClassifier = neighbors.KNeighborsClassifier()

#Fit the data into the Classifier
kNeighborsClassifier = kNeighborsClassifier.fit(X,Y)

#Perform Prediction
kNeighborsClassifierPrediction = kNeighborsClassifier.predict([[161,60,9]])

#Print the Classifier
print(kNeighborsClassifier)

#Print the Prediction
print(kNeighborsClassifierPrediction)



#Define 'GaussianProcessClassifier' Classifier From the imported Tree
gaussianProcessClassifier = gaussian_process.GaussianProcessClassifier()

#Fit the data into the Classifier
gaussianProcessClassifier = gaussianProcessClassifier.fit(X,Y)

#Perform Prediction
gaussianProcessClassifierPrediction = gaussianProcessClassifier.predict([[161,60,9]])

#Print the Classifier
print(gaussianProcessClassifier)

#Print the Prediction
print(gaussianProcessClassifierPrediction)