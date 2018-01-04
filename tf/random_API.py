"""
1.  tf.random_normal() 从正态分布中输出随机值
2.  tf.random_poisson() 从每个给定的泊松分布中绘制形状样本。
3.  tf.random_uniform() 从均匀分布中输出随机值。
4.  tf.random_shuffle() 沿着它的第一维随机洗牌张量。自己理解：每列随机打乱

random_normal(
    shape,
    mean=0.0,
    stddev=1.0,
    dtype=tf.float32,
    seed=None,
    name=None
)

random_shuffle(
    value,
    seed=None,
    name=None
)

5.  tf.random_gamma() 从每个给定的Gamma分布中绘制形状样本。
"""
#!/usr/bin/env python
import tensorflow as tf
import numpy as np


randNormal = tf.random_normal([2, 2])
# 创建给定形状的数组，并用[0,1]上的均匀分布的随机样本填充它。
rand = np.random.rand(3, 2)
randShuffle = tf.random_shuffle(rand)
print(rand)

print(randNormal)
with tf.Session() as sess:
    print(sess.run(randNormal))
    print(sess.run(randShuffle))
