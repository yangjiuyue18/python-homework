# 将数组 A "展平" 成一个一维数组，并且只保留其中的唯一元素，保持它们在数组中出现的顺序不变。使用 np.unique() 函数。

import numpy as np

A = np.random.randint(0, 100, size=(200,50))

A_flatten = A.flatten()

A_array, index  = np.unique(A_flatten, return_index=True)

A_unique = A_flatten[np.sort(index)]

print(A_unique)