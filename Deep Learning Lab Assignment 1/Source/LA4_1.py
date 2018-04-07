import tensorflow as tf
import numpy as np
#Importing load_breast_cancer from sklearn datasets
from sklearn.datasets import load_breast_cancer
from Sample import pred

dataset = load_breast_cancer()

#Assigning data and target datasets to the define variables
data = dataset.data
labels = dataset.target

labels = np.array(labels).reshape(569, 1)

#Reshaping the array of values to tensor flow values
X = tf.placeholder(tf.float32, shape=[None, 30])
y = tf.placeholder(tf.float32, shape=[None, 1])

tf.set_random_seed(1)

W = tf.Variable(tf.zeros([30, 1]))
b = 0

Z = tf.nn.sigmoid(tf.add(tf.matmul(X, W), b))

#Minimizing error using cross entropy
loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=Z, labels=y))
#Gradient descent
opt = tf.train.GradientDescentOptimizer(learning_rate=0.0001).minimize(loss)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    # Initializing the session
    sess.run(init)
    # Creating the graphs usinf FileWriter method
    writer = tf.summary.FileWriter("./graphs/logistic_reg", sess.graph)

    for i in range(500):

        _, acc = sess.run([opt, loss], feed_dict={X: data, y: labels})

        if i % 50 == 0:
            # Displaying cost reduction for each iteration
            print("cost: " + str(acc))

    writer.close()
    weights = sess.run(W)
outs = pred(data, weights) #Calling the function
#Calculating accuracy score for the regression model
print("Accuracy Score is: {} %".format(100 - np.mean(np.abs(outs - labels)) * 100))


