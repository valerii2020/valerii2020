# a,b,c - произвольные числа, D - дискриминант выражения
print("Для решения квадратного уравнения ax²+bx+c=0 ведите:")
a = input("значение а")
b = input("начение b")
c = input("значение c")
a = float(a)
b = float(b)
c = float(c)

D = (b ** 2) - 4 * a * c

x1 = (-b + (D ** 0.5))/2 * a
x2 = (-b - (D ** 0.5))/2 * a

print("Для Ваших исходных данных результат составляет", "значение x1=", x1, "значение x2=", x2)
