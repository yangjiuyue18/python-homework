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
             
    def __rsub__(self, other: Union["Dual", Number]) -> "Dual":
         match other:
            case Dual(o_value, o_d):
                return Dual(o_value - self.value, o_d - self.d)
            case Number():
                return Dual(float(other) - self.value, -self.d)

    def __float__(self):
        return self.value

    __rmul__ = __mul__
    __radd__ = __add__

def cos(x: Union[Dual, Number]) -> Dual:
    if isinstance(x, Dual):
        return Dual(math.cos(x.value), -math.sin(x.value)*x.d)
    else:
        return Dual(math.cos(x), 0)

def sin(x: Union[Dual, Number]) -> Dual:
    if isinstance(x, Dual):
        return Dual(math.sin(x.value), math.cos(x.value)*x.d)
    else:
        return Dual(math.sin(x), 0)

def exp(x: Union[Dual, Number]) -> Dual:
    if isinstance(x, Dual):
        return Dual(math.exp(x.value), math.exp(x.value)*x.d)
    else:
        return Dual(math.exp(x), 0)

def log(x: Union[Dual, Number]) -> Dual:
    if isinstance(x, Dual):
        return Dual(math.log(x.value), x.d/x.value)
    else:
        return Dual(math.log(x), 0)


def diff(func: Callable[[float], float]) -> Callable[[float], float]:
    return lambda x: func(Dual(x, 1.0)).d

def f(x: Dual) -> Dual:
    return x + 5*x - cos(20 * log(12 - 20*x*x)) - 20*x

df = diff(f)
print(df(-0.5))  # 输出f在x=-0.5处的导数  39.644950968544144
