"""
placeholder(
    dtype,
    shape=None,
    name=None
)
参数:
    dtype: 初始化的数据类型
    shape: 张量的形状（可选）。如果未指定形状，则可以输入任何形状的张量。
    name: 操作的名称
返回:
    一个张量，可以在处理器中被赋值使用，但不直接赋值
使用方法：
1. tf.placeholder(tf.float32, shape=(1024, 1024)) 指定shape
2. tf.placeholder(tf.float32, [None, 100]) 不指定行 Tensor("Placeholder:0", shape=(?, 100), dtype=float32)
3. 可以通过list或tuple指定shape的性质

https://www.tensorflow.org/versions/r1.3/api_docs/python/tf/placeholder
"""
# !/usr/bin/env python
import tensorflow as tf
import numpy as np

# x = tf.placeholder(tf.float32, shape=(1024, 1024))
x = tf.placeholder(tf.float32, [1024, 1024])
print(x)
y = tf.matmul(x, x)

with tf.Session() as sess:
    # print(sess.run(y))  # ERROR: will fail because x was not fed.

    rand_array = np.random.rand(1024, 1024)
    print(sess.run(y, feed_dict={x: rand_array}))  # Will succeed.
