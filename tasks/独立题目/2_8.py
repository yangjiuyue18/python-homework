# 计算数组 A 中所有元素都大于 5 的行的数量。使用 np.all() 方法。


import numpy as np

A = np.random.randint(0, 100, size=(200, 50))

# 步骤 1: 创建一个布尔数组，其中元素表示 A 中的元素是否大于 5
A_5 = A > 5

# 步骤 2: 使用 np.all() 检查哪些行的所有元素都大于 5
all_5 = np.all(A_5, axis=1)

# 步骤 3: 统计满足条件的行数
A_all_5 = np.sum(all_5)
