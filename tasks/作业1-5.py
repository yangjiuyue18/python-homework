from dataclasses import dataclass
from typing import Union, Callable, List
from numbers import Number
import re

@dataclass
class Dual:
    values: List[float]
    d: float

    def __add__(self, other: Union["Dual", Number]) -> "Dual":
        match other:
            case Dual(o_values, o_d):
                return Dual([self.values[i] + o_values[i] for i in range(len(self.values))], self.d + o_d)
            case Number():
                return Dual([float(other) + self.values[i] for i in range(len(self.values))], self.d)

    def __sub__(self, other: Union["Dual", Number]) -> "Dual":
        match other:
            case Dual(o_values, o_d):
                return Dual([self.values[i] - o_values[i] for i in range(len(self.values))], self.d - o_d)
            case Number():
                return Dual([self.values[i] - float(other) for i in range(len(self.values))], self.d)

    def __mul__(self, other: Union["Dual", Number]) -> "Dual":
        match other:
            case Dual(o_values, o_d):
                new_values = [self.values[i] * o_values[i] for i in range(len(self.values))]
                new_d = sum([self.d * o_values[i] + self.values[i] * o_d for i in range(len(self.values))])
                return Dual(new_values, new_d)
            case Number():
                new_values = [float(other) * self.values[i] for i in range(len(self.values))]
                return Dual(new_values, float(other) * self.d)

    def __truediv__(self, other: Union["Dual", Number]) -> "Dual":
        match other:
            case Dual(o_values, o_d):
                new_values = [self.values[i] / o_values[i] for i in range(len(self.values))]
                new_d = sum([(self.d * o_values[i] - self.values[i] * o_d) / (o_values[i] * o_values[i]) for i in range(len(self.values))])
                return Dual(new_values, new_d)
            case Number():
                new_values = [self.values[i] / float(other) for i in range(len(self.values))]
                new_d = self.d / float(other)
                return Dual(new_values, new_d)

    def __pow__(self, exponent: Union["Dual", Number]) -> "Dual":
        match exponent:
            case Dual(e_values, e_d):
                new_values = [self.values[i] ** e_values[i] for i in range(len(self.values))]
                new_d = sum([self.d * e_values[i] * self.values[i] ** (e_values[i] - 1) for i in range(len(self.values))]) + sum([e_d * new_values[i] for i in range(len(new_values))])
                return Dual(new_values, new_d)
            case Number():
                new_values = [self.values[i] ** float(exponent) for i in range(len(self.values))]
                new_d = sum([self.d * float(exponent) * self.values[i] ** (float(exponent) - 1) for i in range(len(self.values))])
                return Dual(new_values, new_d)

    __rmul__ = __mul__
    __radd__ = __add__

def diff(func: Callable[[List[float]], float]) -> Callable[[List[float]], float]:
    return lambda args: func(Dual(args, 1.0)).d

# 获取用户输入的函数表达式
expression = input("请输入函数表达式（使用 x, y, z 作为变量）：")

# 处理幂指数大于等于1的情况
expression = re.sub(r'(\d+)\s*/\s*x\s*\*\*\s*([1-9]+)', r'\1*x**-\2', expression)
expression = re.sub(r'(\d+)\s*/\s*y\s*\*\*\s*([1-9]+)', r'\1*y**-\2', expression)
expression = re.sub(r'(\d+)\s*/\s*z\s*\*\*\s*([1-9]+)', r'\1*z**-\2', expression)

# 处理幂指数为1或没有幂指数的情况
expression = re.sub(r'(\d+)\s*/\s*(x(?!\*\*))', r'\1*x**-1', expression)
expression = re.sub(r'(\d+)\s*/\s*(y(?!\*\*))', r'\1*y**-1', expression)
expression = re.sub(r'(\d+)\s*/\s*(z(?!\*\*))', r'\1*z**-1', expression)

# print(expression)

# 获取用户输入的 x, y, z 值
x_value = float(input("请输入 x 的值："))
y_value = float(input("请输入 y 的值："))
z_value = float(input("请输入 z 的值："))

# 定义要求导的函数
def f(x: float, y: float, z: float) -> float:
    # 检查 x, y, z 是否 are in denominators
    if "x**-" in expression and x_value == 0:
        raise ValueError("x 不能为零，因为它是分母")
    if "y**-" in expression and y_value == 0:
        raise ValueError("y 不能为零，因为它是分母")
    if "z**-" in expression and z_value == 0:
        raise ValueError("z 不能为零，因为它是分母")

    # 使用用户输入的表达式计算值
    result = eval(expression)
    return result

try:
    f_diff = diff(f)
    result = f_diff([x_value, y_value, z_value])
    print(f"函数在 (x = {x_value}, y = {y_value}, z = {z_value}) 处的导数为：{result}")
except ValueError as e:
    print(e)
