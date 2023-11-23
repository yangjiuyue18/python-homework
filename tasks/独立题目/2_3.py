import numpy as np


#找到数组A中那一行的索引，该行中元素的最大值和最小值之差是所有行中最大的。


A = np.random.randint(0, 100, size=(200, 50))

# 计算每一行的最大值和最小值
max_per_row = A.max(axis=1)
min_per_row = A.min(axis=1)

# 计算每一行的最大值和最小值之差
difference = max_per_row - min_per_row

# 找到最大差值的行索引
max_diff_index = np.argmax(difference)

print(max_per_row)
max_diff_index  # 显示行索引