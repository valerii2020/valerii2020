print("В калькуляторе вы можете воспользоваться функциями:")
print("+", "-", "*", "/", "**")
print("sin", "cos", "tg")
import math
c = None
a = None
b = None
f = None
d = input("введите операцию, которую хотите совершить")
if d == '+' or d == '-' or d == '*' or d == "/":
    a = float(input('введите первое число'))
    b = float(input('введите второе число'))
elif d == '**':
    a = int(input('введите число, которое нужно возвести в степень'))
    b = int(input('введите число степени функции'))
else:
    f = int(input('введите значение в градусах для расчета тригонометрической функции'))
    f = math.radians(f)
if d == '+':
    c = a + b
elif d == '-':
    c = a - b
elif d == '*':
    c = a * b
elif d == '/':
    c = a / b
elif d == '**':
    c = a ** b
else:
    if d == 'sin':
        c = float(math.sin(f))
    elif d == 'cos':
        c = float(math.cos(f))
    else:
        c == float(math.tan(f))
print('ваш результат', c)






