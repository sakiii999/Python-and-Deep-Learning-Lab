#Importing libraries
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.svm import SVC
#Defining and assigning data and target variables
dd=datasets.load_iris() #Iris dataset is used from scipy datasets
info=dd.data
labeldata=dd.target
xtrain,xtest,ytrain,ytest=train_test_split(info,labeldata,test_size=0.2,random_state=62)
xtrain1,xtest1,ytrain1,ytest1=train_test_split(info,labeldata,test_size=0.2,random_state=30)
svc=SVC(kernel='linear') #Applying SVC to linear kernel
svc1=SVC(kernel='rbf') #Applying SVC to rbf kernel
svc.fit(xtrain,ytrain)
yprediction=svc.predict(xtest)
print("The accuracy score for linear kernel is ",accuracy_score(yprediction,ytest)) #Calculating accuracy score after applying SVC to linear kernel
print(yprediction)

svc1.fit(xtrain1,ytrain1)
yprediction1=svc.predict(xtest1)
print("The accuracy score RBF kernel is ",accuracy_score(yprediction1,ytest1)) #Calculating accuracy score after applying SVC to linear kernel
print(yprediction1)