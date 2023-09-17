from scipy.misc import derivative

def f(x: float) -> float:
    return 5 * x * x + 2 * x + 2

print(derivative(f, 2.))