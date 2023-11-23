# 将数组 A 展平成一个一维数组。创建三个新的数组，分别计算窗口大小为 3、5 和 10 的滑动平均值。
# 然后计算这些数组的和，将它们对齐时，右侧用零填充以匹配数组的大小。
# np.cumsum() / np.convolve()

import numpy as np

def moving(arr, window):
    A_cumsum = np.cumsum(arr, dtype=float)
    A_cumsum[window:] = A_cumsum[window:] - A_cumsum[:-window]
    return A_cumsum[window - 1:] / window

A = np.random.randint(0, 100, size=(200, 50))

A_flatten = A.flatten()

A3 = moving(A_flatten, 3)
A5 = moving(A_flatten, 5)
A10 = moving(A_flatten, 10)

max_len = max(len(A3), len(A5), len(A10))

B3 = np.zeros(max_len)
B5 = np.zeros(max_len)
B10 = np.zeros(max_len)

B3[:len(A3)] = A3
B5[:len(A5)] = A5
B10[:len(A10)] = A10

sum_A = B3 + B5 + B10

print(sum_A)

