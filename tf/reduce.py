#!/usr/bin/env python

import tensorflow as tf
import numpy as np

x = [[1.0, 1.0], [2.0, 2.0], [3.0, 3.0]]
average = tf.reduce_mean(x)
averageLine = tf.reduce_mean(x, [0])
averageRow = tf.reduce_mean(x, [1])
m = np.array([[1., 1.], [2., 2.], [3., 3.]])
averageNP = np.mean(m)
xs = tf.placeholder(tf.float32, [32, 1])

print(xs)
print(np.mean(x))

sess = tf.Session()
print(x)
print(m)
print(sess.run(average))
print(sess.run(averageLine))
print(sess.run(averageRow))
print(averageNP)

