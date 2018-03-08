#Importing libraries
import matplotlib.pyplot as plt
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
lda=LinearDiscriminantAnalysis() #Applying linear discriminant analysis
#logistic=LogisticRegression() #Applying logistic regression
a=lda.fit(xtrain,ytrain)
yprediction=lda.predict(xtest) #Predicting the outcomes

#a=logistic.fit(xtrain,ytrain)
#yprediction=logistic.predict(xtest) #Predicting the outcomes
#Calculating the accuracy score by applying LDA model
print("The accuracy score is ",accuracy_score(yprediction,ytest))

plt.figure()
colours = ['red', 'black', 'yellow']
for x, y, z in zip(colours, [0, 1, 2], dd):
    plt.scatter(a[labeldata == y, 0], a[labeldata == y, 1], alpha=.8, color=x,
                label=z)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('LDA for the given dataset is')
plt.show()