#!/usr/bin/env python


import random
# random.sample的函数原型为：random.sample(sequence, k)，从指定序列中随机获取指定长度的片断。sample函数不会修改原有序列。
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
slice = random.sample(list, 5)  #从list中随机获取5个元素，作为一个片断返回
# [1, 9, 10, 4, 5]
# [7, 10, 9, 4, 2]

p = ["Python", "is", "powerful", "simple", "and so on..."]
random.shuffle(p)
# ['simple', 'is', 'Python', 'and so on...', 'powerful']

random.random()
# 用于生成一个0到1的随机符点数: 0 <= n < 1.0 输出:0.8490716344202429

random.uniform(10, 20)
# 用于生成一个指定范围内的随机符点数，两个参数其中一个是上限，一个是下限。如果a > b，则生成的随机数n: a <= n <= b。如果 a <b， 则 b <= n <= a。
# 19.519845738021708

random.randint(12, 20)
# ：random.randint(a, b)，用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b
# 16

random.randrange(10, 100, 2)
# random.randrange([start], stop[, step])，从指定范围内，
# 按指定基数递增的集合中 获取一个随机数。如：random.randrange(10, 100, 2)，
# 结果相当于从[10, 12, 14, 16, ... 96, 98]序列中获取一个随机数。random.randrange(10, 100, 2)
# 在结果上与 random.choice(range(10, 100, 2) 等效。

random.choice("学习Python")
random.choice(["JGood", "is", "a", "handsome", "boy"])
random.choice(("Tuple", "List", "Dict"))
# random.choice(sequence)random.choice从序列中获取一个随机元素

