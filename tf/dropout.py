#!/usr/bin/env python


import tensorflow as tf

input_batch = tf.constant(
    [
        [
            [[1.0], [0.0], [0.0], [0.0], [0.0], [1.0]],
            [[0.0], [1.0], [0.0], [0.0], [1.0], [0.0]],
            [[0.0], [0.0], [1.0], [1.0], [0.0], [0.0]],
            [[1.0], [0.0], [0.0], [0.0], [1.0], [0.0]],
            [[0.0], [1.0], [0.0], [0.0], [1.0], [0.0]],
            [[0.0], [0.0], [1.0], [0.0], [1.0], [0.0]]
        ]
    ])
kernel = tf.constant([
    [[[1.0]], [[-1.0]], [[-1.0]]],
    [[[-1.0]], [[1.0]], [[-1.0]]],
    [[[-1.0]], [[-1.0]], [[1.0]]]
])
tf.global_variables()
with tf.Session() as sess:
    conv2d = tf.nn.conv2d(input_batch,
                          kernel,
                          strides=[1, 1, 1, 1],
                          padding='SAME')
    print(sess.run(conv2d))
    print('------')
    print(sess.run(conv2d))
    print(input_batch)
    print(input_batch.shape)
    print(kernel)
    print(kernel.shape)
    print(conv2d.shape)
