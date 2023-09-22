from scipy.misc import derivative

from typing import Callable

# f′(x)≈ f(x+ϵ)−f(x−ϵ)​/2ϵ


def numerical_derivative(func: Callable[[float], float], x: float, epsilon: float = 1e-6) -> float:

    f_x_plus_epsilon = func(x + epsilon)
    f_x_minus_epsilon = func(x - epsilon)
    
    numerical_derivative = (f_x_plus_epsilon - f_x_minus_epsilon) / (2 * epsilon)
    
    return numerical_derivative

# 获取用户输入的函数表达式
expression = input("请输入函数表达式（使用 x 作为变量）：")

# 获取用户输入的 x 值
x_value = float(input("请输入 x 的值："))

# 定义要求导的函数
def f(x: float) -> float:
    # 检查 x 是否为分母
    if "/x" in expression:
        if x_value == 0:
            raise ValueError("x 不能为零，因为它是分母")
    
    # 使用用户输入的表达式计算值
    result = eval(expression)
    return result

try:
    result = numerical_derivative(f,x_value)
    print(f"函数在 x = {x_value} 处的导数为：{result}")
except ValueError as e:
    print(e)


# def f(x: float) -> float:
#     return 5 * x * x + 2 * x + 2

# print(derivative(f, 2.))