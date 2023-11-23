# 重构给定的抽样算法，使其更高效，使用 NumPy 数组而不使用循环，并通过统计测试验证新旧算法的一致性。


import numpy as np
from typing import List
from scipy.stats import chisquare

# 原始的 sample 函数
def sample(x: List[int], c: int) -> List[int]:
    assert len(x) > 0
    
    s = np.sum(x)
    res = []
    for _ in range(c):
        val = s * np.random.random()
        cur, idx = 0, 0        
        while cur + x[idx] <= val:
            cur += x[idx]
            idx += 1
            
        res.append(idx)
    return res

# 优化后的 sample 函数
def optimized_sample(x: List[int], c: int) -> List[int]:
    assert len(x) > 0

    s = np.sum(x)
    x_cumsum = np.cumsum(x)
    random_values = np.random.random(c) * s
    sample_indices = np.searchsorted(x_cumsum, random_values)

    return list(sample_indices)

# 测试两个函数并进行卡方检验
def test_sampling_methods():
    # 生成大量的样本来进行比较
    original_samples = sample([50, 3, 1, 7, 20], 1000)
    optimized_samples = optimized_sample([50, 3, 1, 7, 20], 1000)

    # 计算每个索引的出现次数
    original_freq = np.bincount(original_samples, minlength=len([50, 3, 1, 7, 20]))
    optimized_freq = np.bincount(optimized_samples, minlength=len([50, 3, 1, 7, 20]))

    # 进行卡方检验
    chi_stat, p_value = chisquare(original_freq, f_exp=optimized_freq)

    return chi_stat, p_value

# 运行测试
chi_stat, p_value = test_sampling_methods()
chi_stat, p_value

