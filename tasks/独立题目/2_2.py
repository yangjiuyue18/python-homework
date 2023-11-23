import numpy as np

# 生成一个新数组，该数组仅包含数组A中的那些行，满足以下条件：
# 在偶数索引列（索引0, 2, ...）上元素的总和大于所有行在奇数索引列（索引1, 3, ...）上元素总和的平均值。


A = np.random.randint(0, 100, size=(200, 50))

# 计算奇数列和偶数列的和
sum_even_columns = A[:, 0::2].sum(axis=0)  # 偶数列（从0开始，步长为2）的和
sum_odd_columns = A[:, 1::2].sum(axis=0)   # 奇数列（从1开始，步长为2）的和

# 计算奇数列和的平均值
average_sum_odd_columns = sum_odd_columns.mean()

# 选择满足条件的行：偶数列的和大于奇数列的和的平均值
selected_rows = A[sum_even_columns > average_sum_odd_columns]

# selected_rows 现在是满足条件的行
