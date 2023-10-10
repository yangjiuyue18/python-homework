import math
from typing import Callable

# f′(x)≈ f(x+ϵ)−f(x−ϵ)​/2ϵ

def numerical_derivative(func: Callable[[float], float], x: float, epsilon: float = 1e-6) -> float:
    f_x_plus_epsilon = func(x + epsilon)
    f_x_minus_epsilon = func(x - epsilon)
    
    numerical_derivative = (f_x_plus_epsilon - f_x_minus_epsilon) / (2 * epsilon)
    
    return numerical_derivative

def test_numerical_derivative():
    # 定义你提供的函数
    def func(x):
        return x + 5*x - math.cos(20 * math.log(12- 20*x*x)) - 20*x

    # 计算该函数在 x=0.5 处的数值导数
    result = numerical_derivative(func, -0.5)
    
    print(f"The derivative of the function at x=0.5 is {result}")

# 运行测试用例
test_numerical_derivative()

