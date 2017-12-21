#!/usr/bin/env python

import collections
from collections import Counter

"""
Counter是dict的子类，可用于计算可哈希对象。也是一个无序集合，元素存储为dict的key，counts存储为dict的值。Counts允许任何integer的值
包括0或者counts.
https://docs.python.org/2/library/collections.html
"""
# 初始化
c = Counter()  # a new, empty counter
c = Counter('gallahad')  # a new counter from an iterable
c = Counter({'red': 4, 'blue': 2})  # a new counter from a mapping
c = Counter(cats=4, dogs=8)  # a new counter from keyword args
# Counter({'dogs': 8, 'cats': 4})
c = Counter(['eggs', 'ham']) # list
# Counter({'ham': 1, 'eggs': 1})
c['sausage'] = 0
# Counter({'ham': 1, 'eggs': 1, 'sausage': 0})
del c['ham']
# Counter({'eggs': 1, 'sausage': 0}) 实际上移除了map的entry

"""
 Counter除了对所有的字典可以，还支持三种方法
"""

# elements()
# 按照每个元素的计数的次数重复元素，返回一个迭代器，返回元素的顺序是任意的。如果元素的次数比1小，element()会忽略这个元素
c = Counter(a=4, b=2, c=0, d=-2)
list(c.elements())
# ['a', 'a', 'a', 'a', 'b', 'b']

# most_common([n])
# 返回出现次数前n的元素列表，如果n被省略或者为None，则返回Counter的所有元素。出现相同次数的元素的顺序是任一的
c = Counter('abracadabra').most_common(3)
# [('a', 5), ('b', 2), ('r', 2)]

# subtract([iterable-or-mapping])
# 从一个可迭代对象(iterable)或者从一个mapping或者一个Counter中两个元素相减。像dict.update()但是次数相减而不是替代他们。输入或者
# 输出都可能是0或者负数
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
# Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})

"""
count = [['UNK',-1]]
count.extend(collections.Counter(words).most_common(100))
[['UNK',-1],('xiejq',1)]
"""