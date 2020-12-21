x = float(input('для расчета функции введите значение х'))
import math
P = math.pi
if -P <= x <= P:
    y = math.cos(3 * x)
elif x < -P or x > P:
    y = x
print('значение y:', y)

