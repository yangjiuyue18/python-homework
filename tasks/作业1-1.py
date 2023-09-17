from dataclasses import dataclass
from typing import Union, Callable
from numbers import Number
import re

@dataclass
class Dual:
    value: float
    d: float

    def __add__(self, other: Union["Dual", Number]) -> "Dual":
         match other:
            case Dual(o_value, o_d):
                return Dual(self.value + o_value, self.d + o_d)
            case Number():
                return Dual(float(other) + self.value, self.d)
    
    def __sub__(self, other: Union["Dual", Number]) -> "Dual":
         match other:
            case Dual(o_value, o_d):
                return Dual(self.value - o_value, self.d - o_d)
            case Number():
                return Dual(self.value - float(other), self.d)

    def __mul__(self, other: Union["Dual", Number]) -> "Dual":
         match other:
            case Dual(o_value, o_d):
                return Dual(self.value * o_value, self.value * o_d + self.d * o_value)
            case Number():
                return Dual(float(other) * self.value, float(other) * self.d)

    def __truediv__(self, other: Union["Dual", Number]) -> "Dual":
         match other:
            case Dual(o_value, o_d):
                return Dual(self.value / o_value, (self.d * o_value - self.value * o_d) / (o_value * o_value))
            case Number():
                return Dual(self.value / float(other), self.d / float(other))

    def __pow__(self, exponent: Union["Dual", Number]) -> "Dual":
         match exponent:
            case Dual(e_value, e_d):
                new_value = self.value ** e_value
                new_d = (self.d * e_value * self.value ** (e_value - 1)) + (e_d * new_value)
                return Dual(new_value, new_d)
            case Number():
                new_value = self.value ** float(exponent)
                new_d = self.d * float(exponent) * self.value ** (float(exponent) - 1)
                return Dual(new_value, new_d)

    __rmul__ = __mul__
    __radd__ = __add__

def diff(func: Callable[[float], float]) -> Callable[[float], float]:
    return lambda x: func(Dual(x, 1.0)).d

# 获取用户输入的函数表达式
expression = input("请输入函数表达式（使用 x 作为变量）：")

# 处理幂指数大于等于1的情况
expression = re.sub(r'(\d+)\s*/\s*x\s*\*\*\s*([1-9]+)', r'\1*x**-\2', expression)

# 处理幂指数为1或没有幂指数的情况
expression = re.sub(r'(\d+)\s*/\s*(x(?!\*\*))', r'\1*x**-1', expression)

# print(expression)

# 获取用户输入的 x 值
x_value = float(input("请输入 x 的值："))

# 定义要求导的函数
def f(x: float) -> float:
    # 检查 x 是否为分母
    if "x**-" in expression:
        if x_value == 0:
            raise ValueError("x 不能为零，因为它是分母")
    
    # 使用用户输入的表达式计算值
    result = eval(expression)
    return result

try:
    f_diff = diff(f)
    result = f_diff(x_value)
    print(f"函数在 x = {x_value} 处的导数为：{result}")
except ValueError as e:
    print(e)