# 给定一个对 NumPy 数组进行相当奇特操作的函数：
# 请使用以下两种技术中的一种进行优化：
# Numba
# Cython（额外加 5 分）
# Taichi（额外加 5 分）
# Pythran 文档1, 文档2（额外加 2 分）
# 并比较优化前后的性能。

import numpy as np
from numba import jit
import seaborn as sns
import matplotlib.pyplot as plt

# 原始的 strange_conv 函数
def strange_conv(a: np.ndarray) -> np.float64:
    x = a.shape[0]
    y = a.shape[1]

    t = 1.
    for y in range(y - 5):
        for x in range(x - 3):
            c = 1.5 * a[y+1, x+2] - a[y+5, x+3] * a[y, x] + 0.2 * a[y+4, x]
            t = 0.2 * t + 0.8 * c

    return t

# 用 Numba 优化的 strange_conv 函数
@jit
def optimized_strange_conv(a: np.ndarray) -> np.float64:
    x = a.shape[0]
    y = a.shape[1]

    t = 1.
    for y in range(y - 5):
        for x in range(x - 3):
            c = 1.5 * a[y+1, x+2] - a[y+5, x+3] * a[y, x] + 0.2 * a[y+4, x]
            t = 0.2 * t + 0.8 * c

    return t

# 创建测试数组
a = np.random.random((10000, 10000))

# 使用 Jupyter Notebook 的 magic 命令 timeit 测试性能
# %timeit strange_conv(a)
# %timeit optimized_strange_conv(a)

# 运行优化后的函数多次并绘制结果的分布图
num_runs = 100
results = [optimized_strange_conv(a) for _ in range(num_runs)]

# 绘制分布图
plt.figure(figsize=(10, 6))
sns.kdeplot(results, shade=True)
plt.title("Distribution of Optimized Strange Conv Results")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()

