import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()

A = np.random.randint(0, 100, size=(200, 50))


# 生成一个新的数组，其中数组A的列已按随机顺序重新排列。


# 1. 确定列的数量
# .shape 属性来获取数组 A 的形状，它返回一个元组，其中第一个元素是行数，第二个元素是列数。
num = A.shape[1]

# 2. 生成随机列顺序
random_order = np.random.permutation(num)

# 3. 应用随机顺序
A_randomized = A[:, random_order]


print(A_randomized)