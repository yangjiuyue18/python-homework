from dataclasses import dataclass
from typing import Union, Callable, List, Tuple
from numbers import Number

@dataclass
class Dual:
    value: float
    d: float

    def __add__(self, other: Union["Dual", Number]) -> "Dual":
        if isinstance(other, Dual):
            return Dual(self.value + other.value, self.d + other.d)
        elif isinstance(other, Number):
            return Dual(self.value + other, self.d)

    def __sub__(self, other: Union["Dual", Number]) -> "Dual":
        if isinstance(other, Dual):
            return Dual(self.value - other.value, self.d - other.d)
        elif isinstance(other, Number):
            return Dual(self.value - other, self.d)

    def __mul__(self, other: Union["Dual", Number]) -> "Dual":
        if isinstance(other, Dual):
            return Dual(self.value * other.value, self.value * other.d + self.d * other.value)
        elif isinstance(other, Number):
            return Dual(self.value * other, self.d * other)

    def __truediv__(self, other: Union["Dual", Number]) -> "Dual":
        if isinstance(other, Dual):
            return Dual(self.value / other.value, (self.d * other.value - self.value * other.d) / (other.value ** 2))
        elif isinstance(other, Number):
            return Dual(self.value / other, self.d / other)

    def __pow__(self, exponent: Union["Dual", Number]) -> "Dual":
        if isinstance(exponent, Dual):
            new_value = self.value ** exponent.value
            new_d = (self.d * exponent.value * (self.value ** (exponent.value - 1))) + (exponent.d * new_value)
            return Dual(new_value, new_d)
        elif isinstance(exponent, Number):
            new_value = self.value ** exponent
            new_d = exponent * (self.value ** (exponent - 1)) * self.d
            return Dual(new_value, new_d)
    
    def __rsub__(self, other: Union["Dual", Number]) -> "Dual":
         match other:
            case Dual(o_value, o_d):
                return Dual(o_value - self.value, o_d - self.d)
            case Number():
                return Dual(float(other) - self.value, -self.d)

    __rmul__ = __mul__
    __radd__ = __add__

def diff(func: Callable[..., Dual]) -> Callable[..., List[float]]:
    def wrapper(*args, **kwargs):

        for i in range(len(args)):

            dual_args = [Dual(arg, 1 if j == i else 0) for j, arg in enumerate(args)]
            yield func(*dual_args, **kwargs).d

    return wrapper

def f(x: float, y: float, z: float) -> float:
    return x * y + z - 5 * y

f_diff = diff(f)

# 计算在参数 x = 10, y = 10, z = 10 处关于 x、y 和 z 的导数值
for result in f_diff(10,10,10):
    print(result)
# 输出结果应为 [10.0, 5.0, 1.0]
