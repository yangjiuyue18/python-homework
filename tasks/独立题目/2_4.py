# 生成一个与数组 A 相同维度的数组，但是其中的每个元素被替换为该元素在 A 中所有元素升序排列后的序号（从 1 开始）。

# 例如，如果 A 是：
# (12 14
# 1 2)
# (12 1
# ​14 2)
# 那么结果应该是：
# (3 4
# 1 2)
# (3 1
# 4 2)
# *提示：考虑多次应用 [argsort()] 函数。

import numpy as np


A = np.random.randint(0, 100, size=(200, 50))

# 将 A 展平为一维数组
flattened_A = A.flatten()

# 使用 argsort() 获取排序后的索引
sorted_indices = np.argsort(flattened_A)

# 创建一个新数组，其元素是排序位置（从 1 开始计数）
sorted_positions = np.argsort(sorted_indices) + 1

# 将新数组重塑为原始数组 A 的形状 A.shape用于获取原数组的形状
result = sorted_positions.reshape(A.shape)




