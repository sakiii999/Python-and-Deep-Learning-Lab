#Importing libraries
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import neighbors,datasets

#Defining and assigning data and target variables
dd =datasets.load_iris() #Iris dataset is used from scipy datasets
info=dd.data
labeldata=dd.target
#Size of the test data is given 20% and the remaining 80% is defined for training data
xtrain,xtest,ytrain,ytest=train_test_split(info,labeldata,test_size=0.2,random_state=42)
knn=neighbors.KNeighborsClassifier(n_neighbors=1) #Setting the n_neighbors value for KNN
knn.fit(xtrain,ytrain)
yprediction=knn.predict(xtest) #Predicting the outcomes
#Calculating the accuracy score by applying KNN model
print("The accuracy score is ",accuracy_score(yprediction,ytest))