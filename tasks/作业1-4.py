from typing import Callable, Union
from numbers import Number
from dataclasses import dataclass
import math

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

    def sin(self):
        return Dual(math.sin(self.value), math.cos(self.value)*self.d)

    def cos(self):
        return Dual(math.cos(self.value), -math.sin(self.value)*self.d)

    def exp(self):
        return Dual(math.exp(self.value), math.exp(self.value)*self.d)

    def log(self):
        return Dual(math.log(self.value), self.d/self.value)

    __rmul__ = __mul__
    __radd__ = __add__

def diff(func: Callable[[float], float]) -> Callable[[float], float]:
    return lambda x: func(Dual(x, 1.0)).d

def f(x: Dual) -> Dual:
    twelve = Dual(12.0, 0.0)  # 创建一个表示整数12的Dual对象
    # twenty = Dual(20.0, 0.0)  # 创建一个表示整数20的Dual对象

    return x + 5*x - (20 * (twelve - 20*x*x).log()).cos() - 20*x

df = diff(f)
print(df(-0.5))  # 输出f在x=1.0处的导数
