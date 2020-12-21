print("Для решения квадратного уравнения ax²+bx+c=0 ведите:")
a = float(input("значение а"))
b = float(input("начение b"))
c = float(input("значение c"))
x = None
x1 = None
x2 = None
import math

D = (b ** 2) - 4 * a * c

if D < 0:
    print('уравнение не имеет решения')
elif D == 0:
    x == -b / (2 * a)
    print('корень уравнения равен', x)
else:
    x1 = round(((-b + (D ** 0.5))/2 * a), 2)
    x2 = round(((-b - (D ** 0.5))/2 * a), 2)
    print('корни уравнения равны:', x1, x2)
