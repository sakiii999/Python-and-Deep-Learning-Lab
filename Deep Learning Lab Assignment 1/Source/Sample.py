import tensorflow as tf

def pred(X, parameters):
    parameters = tf.convert_to_tensor(parameters)

    x = tf.placeholder(tf.float32, [None, 30])

    z = tf.nn.sigmoid(tf.matmul(x, parameters))

    sess = tf.Session()
    prediction = sess.run(z, feed_dict={x: X})

    return prediction