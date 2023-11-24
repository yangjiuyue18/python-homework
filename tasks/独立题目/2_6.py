# 创建一个新的三维数组，大小为 10×200×50，其中沿着第一个维度（第零轴）的每个子数组是原始二维数组 A 的元素乘以 1 到 10 的系数。

import numpy as np

A = np.random.randint(0, 100, size=(200, 50))

# 创建一个形状为10的一维数组，其元素为1到10
factors = np.arange(1, 11)

# 利用NumPy的广播机制将A乘以factors，得到所需的三维数组
B = A * factors[:, np.newaxis, np.newaxis]
