import numpy as np


# 对数组 A 的每一行应用最小-最大归一化（$\min-\max$ normalization）。也就是说，需要得到一个新的数组，使得每一行中的最大元素等于 1，最小元素等于 0。


A = np.random.randint(0, 100, size=(200, 50))

# 找到每一行的最小值和最大值
min_values = A.min(axis=1, keepdims=True)
max_values = A.max(axis=1, keepdims=True)

# 应用最小-最大归一化
normalized_A = (A - min_values) / (max_values - min_values)