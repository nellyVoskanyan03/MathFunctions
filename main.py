import math
from math_functions import Sin, Cos, Polynomial

pi = math.pi
sqrt = math.sqrt

sin = Sin()
cos = Cos()

tg = sin/cos
print(tg(pi/4))  # 1.0

tg_derivative = tg.derivative()
print(tg_derivative(pi/4))  # 2.0

x_2 = Polynomial(0, 0, 1)  # 0*1 + 0*x + 1*x^2
print(x_2)

p = Polynomial({3: 3, 1: 5, 2: 4}) # 3*x^3 + 5*x + 4*x^2
print(p)
print(x_2 * p) # 5*x^3 + 4*x^4 + 3*x^5

print(x_2(12))  # 144

sin_2 = x_2.combine(sin)  # sin^2 (x)
print(sin_2(3 * pi / 2))  # 1.0

cos_x_2 = cos.combine(x_2)  # cos(x^2)
print(cos_x_2(-sqrt(pi)))  # -1.0

print(Polynomial(1, 0, 1).combine(Sin()))  # sin(x)^2 + 1
