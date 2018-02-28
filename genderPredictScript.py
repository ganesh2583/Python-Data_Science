from sklearn import tree

#[height, weight, shoe size]
X = [[181,80,44],[565,57,57],[131,57,75],[32,35,576],[75,57,57],[57,34,57],[34,34,34],[87,97,55],[45,67,54],[23,80,64],[77,57,23]]
#Gender
Y = ['female','female','male','female','male','male','male','male','female','female','female']

#Define Classifier From the imported Tree
classifier = tree.DecisionTreeClassifier()

#Fit the data into the Classifier
classifier = classifier.fit(X,Y)

#Perform Prediction
prediction = classifier.predict([[10,67,90]])

#Print the Classifier
print(classifier)

#Print the Prediction
print(prediction)