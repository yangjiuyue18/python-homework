from math import sin,cos,log,exp
from typing import Callable,Iterable,Generator

# f′(x)≈ f(x+ϵ)−f(x−ϵ)​/2ϵ

def numerical_derivative(func: Callable[[float], float], xs: Iterable[float], epsilon: float = 1e-6) -> Generator[float,None,None]:

    for x in xs:

        f_x_plus_epsilon = func(x + epsilon)
        f_x_minus_epsilon = func(x - epsilon)
    
        numerical_derivative = (f_x_plus_epsilon - f_x_minus_epsilon) / (2 * epsilon)
    
        yield numerical_derivative

def func(x :float) -> float:
    return x + 5*x - cos(20 * log(12- 20*x*x)) - 20*x

# 运行测试用例
xs= [-0.5, 0, 0.5]
for test in numerical_derivative(func,xs):
    print(test)

