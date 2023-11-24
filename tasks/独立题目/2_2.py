import numpy as np

# 生成一个新数组，它只包含数组 A 中满足以下条件的行：其中偶数列（索引 0,2,…0,2,…）的元素之和大于整个数组中奇数列（索引 1,3,…1,3,…）的元素之和的平均值。


A = np.random.randint(0, 100, size=(200, 50))

# 计算奇数列和偶数列的和
sum_even_columns = A[:, 0::2].sum(axis=1)  # 偶数列（从0开始，步长为2）的和
sum_odd_columns = A[:, 1::2].sum(axis=1)   # 奇数列（从1开始，步长为2）的和

# 计算奇数列和的平均值
average_sum_odd_columns = sum_odd_columns.mean()

# 选择满足条件的行：偶数列的和大于奇数列的和的平均值
selected_rows = A[sum_even_columns > average_sum_odd_columns]