# 创建一个一维数组，其大小为 200，其中每个元素是数组 A 中相应行与 A 的“平均”行之间的欧几里得距离。


import numpy as np

A = np.random.randint(0, 100, size=(200,50))

A_mean = np.mean(A, axis=0)

B = np.sqrt(np.sum((A - A_mean)**2, axis = 1))

print(B)