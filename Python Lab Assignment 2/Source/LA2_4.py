import numpy as np
#Creates a list of array wit size 15 and range in between 0 to 20
random = np.random.randint(low=0,high=20,size=15)
print("The random vector is",random)
#Total count of each integer are calculated using bincount method
totalcount = np.bincount(random)
#Most occurences of an integer i.e. highest count is returned using argmax method
print("Most frequent item in the list is",np.argmax(totalcount))