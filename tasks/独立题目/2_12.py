# 创建一个新数组，该数组由数组 A 的元素组成，但根据以下规则修改了这些元素：
# 如果元素小于 50，那么它被乘以 2。
# 否则，它被乘以 3。
# np.where()

import numpy as np

A = np.random.randint(0, 100, size=(200, 50))

A_where = np.where(A < 50, A*2, A*3)