from dataclasses import dataclass
from typing import Union, Callable, Iterable,Generator
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
             
    def __rsub__(self, other: Union["Dual", Number]) -> "Dual":
         match other:
            case Dual(o_value, o_d):
                return Dual(o_value - self.value, o_d - self.d)
            case Number():
                return Dual(float(other) - self.value, -self.d)

    __rmul__ = __mul__
    __radd__ = __add__

def diff(func: Callable[[float], float], xs = Iterable[float]) -> Generator[float, None,None]:
    for x in xs:
        yield func(Dual(x, 1.0)).d

# Функция, которую будем дифференцировать
def f(x: float) -> float:
    return 5 * x * x + 2 * x + 2

# значение производной в точке x = 2
xs =[-2,-1,1,2]
for test in diff(f,xs):
    print(test)