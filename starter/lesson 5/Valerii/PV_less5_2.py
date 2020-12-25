def kv(x):
    y = x ** 2
    return y

def kn(x):
    y = x * 0.5
    return y
print('результаты расчета функций х² и √x в диапозоне от х=-5 до х=5 с шагом 0.5')
print()

print('x        ', 'квадрат x    ', 'корень x')

import numpy as np
np.arange(-5, 5, 0.5)

for i in np.arange(-5, 5, 0.5):
    m = kv(i)
    n = kn(i)
    print(i, '      ', m, '      ', n)



