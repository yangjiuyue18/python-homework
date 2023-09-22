import math

# 实现自定义的exp函数
# 计算每一项 x^i / i! 并将其添加到结果中，其中 i 逐渐增加。
def custom_exp(x):
    result = 0
    for i in range(20):  # 计算前20个项的级数展开
        numerator = x ** i
        denominator = math.factorial(i)
        result += numerator / denominator
    return result

# 实现自定义的cos函数
# 这里使用了前10项的泰勒级数[(-1)^i*x**(2i)]/2i!来计算 cos(x)。
# 其中，sign 表示正负号，numerator 表示分子，denominator 表示分母。math.factorial(n) 函数表示计算 n 的阶乘。
def custom_cos(x):
    result = 0.0
    for i in range(10):
        sign = (-1) ** i
        numerator = x ** (2 * i)
        denominator = math.factorial(2 * i)
        result += sign * numerator / denominator
    return result

# 实现自定义的sin函数
# 这里使用了前10项的泰勒级数[(-1)^i*x**(2i+1)]/(2i+1)!来计算 sin(x)。
# 其中，sign 表示正负号，numerator 表示分子，denominator 表示分母。math.factorial(n) 函数表示计算 n 的阶乘。
def custom_sin(x):
    result = 0.0
    for i in range(10):
        sign = (-1) ** i
        numerator = x ** (2 * i + 1)
        denominator = math.factorial(2 * i + 1)
        result += sign * numerator / denominator
    return result

# 实现自定义的log函数（自然对数）
# 使用交替的正负号，计算每一项 ((-1)^(i - 1)) * (x - 1)^i / i 并将其添加到结果中，其中 i 逐渐增加。
def custom_log(x):
    result = 0
    for i in range(1,1001):
        sign = (-1) ** (i -1)
        numerator = (x - 1) ** i
        result += sign * numerator / i
    return result

# 使用示例：
x = 2
print(math.exp(x))
print(f"exp({x}) = {custom_exp(x)}")
print(math.cos(x))
print(f"cos({x}) = {custom_cos(x)}")
print(math.sin(x))
print(f"sin({x}) = {custom_sin(x)}")
print(math.log(x))
print(f"log({x}) = {custom_log(x)}")
