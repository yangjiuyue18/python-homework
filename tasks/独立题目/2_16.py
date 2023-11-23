# 给定以下“随机漫步”算法：使用 numpy 实现一个更高效的版本，并比较两个版本的性能（可以使用 timeit 魔术命令）。
# 利用 seaborn 库中的 kdeplot() 或类似函数，绘制 walk(10_000) 在一定次数运行后的值分布图。

import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns

# 原始的 walk 函数
def walk(n: int):
    cur_position = 0
    for _ in range(n):
        cur_position += random.choice([-3, -1, 0, 2, 3])
    return cur_position

# 优化后的 walk 函数
def optimized_walk(n: int):
    steps = np.random.choice([-3, -1, 0, 2, 3], size=n)
    return np.sum(steps)

# 测试两个函数的性能
# 使用 Jupyter Notebook 的 magic 命令 timeit
# %timeit walk(10_000)
# %timeit optimized_walk(10_000)

# 运行 walk(10_000) 多次并绘制结果的分布图
num_runs = 1000
walk_results = [optimized_walk(10_000) for _ in range(num_runs)]

# 绘制分布图
plt.figure(figsize=(10, 6))
sns.kdeplot(walk_results, shade=True)
plt.title("Distribution of Walk(10,000) Results")
plt.xlabel("Final Position")
plt.ylabel("Density")
plt.show()

