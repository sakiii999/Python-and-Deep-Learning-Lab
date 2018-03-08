#Importing libraries
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
#Defining and assigning data and target variables
dd=load_digits() #Dataset load_digits is used from scipy datasets
info=dd.data
labeldata=dd.target
#Size of the test data is given 20% and the remaining 80% is defined for training data
xtrain,xtest,ytrain,ytest=train_test_split(info,labeldata,test_size=0.2,random_state=30)
#lda=LinearDiscriminantAnalysis() #Applying linear discriminant analysis
logistic=LogisticRegression() #Applying logistic regression
#lda.fit(xtrain,ytrain)
#yprediction=lda.predict(xtest) #Predicting the outcomes

logistic.fit(xtrain,ytrain)
yprediction=logistic.predict(xtest) #Predicting the outcomes
#Calculating the accuracy score by applying LDA model
print("The accuracy score is ",accuracy_score(yprediction,ytest))