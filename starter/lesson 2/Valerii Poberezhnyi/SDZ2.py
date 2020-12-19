# a,b,x - целые числа, S - результат задачи

a = input("введите целое число а")
b = input("введите целое число b")
x = input("введите целое число x")
a = int(a)
b = int(b)
x = int(x)

s = None

if a < x < b:
    S = True
else:
    S = False

print("итоговое значение:", S)
