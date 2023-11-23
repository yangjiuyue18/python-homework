# 绘制函数 f(x) = (5*sin(2x) - cos^2(x) - 1 + |x^3| - x^2) / (x^2 + 1)及其导数的图像。
# 使用 scipy 找到函数的最小值，并在图上标出。在同一坐标轴上，绘制这个函数的窗口大小为 1、2、5 的滑动平均的图像。

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar
from scipy.misc import derivative

# 定义函数 f(x)
def f(x):
    return (5 * np.sin(2 * x) - np.cos(x)**2 - 1 + np.abs(x**3) - x**2) / (x**2 + 1)

# 定义求导函数
def df(x):
    return derivative(f, x, dx=1e-6)

# 寻找函数的最小值
result = minimize_scalar(f)
min_x = result.x
min_y = f(min_x)

# 创建 x 轴数据点
x = np.linspace(-10, 10, 400)
y = f(x)
dy = df(x)

# 计算滑动平均
def moving_average(arr, window):
    return np.convolve(arr, np.ones(window)/window, mode='valid')

y_ma1 = moving_average(y, 1)
y_ma2 = moving_average(y, 2)
y_ma5 = moving_average(y, 5)

# 绘制函数 f(x) 和它的导数
plt.figure(figsize=(12, 6))
plt.plot(x, y, label='f(x)')
plt.plot(x, dy, label="f'(x)")
plt.plot(x[0:len(y_ma1)], y_ma1, label='MA-1')
plt.plot(x[0:len(y_ma2)], y_ma2, label='MA-2')
plt.plot(x[0:len(y_ma5)], y_ma5, label='MA-5')

# 标记最小值
plt.scatter(min_x, min_y, color='red')
plt.text(min_x, min_y, f'Minimum ({min_x:.2f}, {min_y:.2f})', color='red')

# 设置图表标签和图例
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Function f(x) and Its Derivative with Moving Averages')
plt.legend()
plt.grid(True)
plt.show()

