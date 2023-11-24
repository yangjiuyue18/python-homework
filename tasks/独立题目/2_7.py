# 创建一个与数组 A 相同维度的新数组，这个数组首先包含 A 的所有偶数列，然后是所有奇数列。使用 np.concat() 方法。

import numpy as np

A = np.random.randint(0, 100, size=(200, 50))

#提取偶数列
even_columns = A[:, ::2]

# 提取奇数列
odd_columns = A[:, 1::2]

new_A = np.concatenate((even_columns,odd_columns), axis=1)
