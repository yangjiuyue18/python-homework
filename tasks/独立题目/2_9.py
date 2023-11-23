# 将数组 A 水平地分割成 10 个部分，然后创建一个新的数组，其尺寸为 20×50，这个新数组是这些部分的平均值。使用 np.split() 方法。


import numpy as np

A =  np.random.randint(0, 100, size=(200,50))

A_split = np.split(A, 10)

A_mean = np.sum(A_split, axis=0) / 10

print(A_mean)