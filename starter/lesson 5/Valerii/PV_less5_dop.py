def sr(x, y, z):
    c = (x + y + z) / 3
    return c

print('программа вычисления среднего арифмитического трех чисел')
print()

vv = " "
while vv != 'stop':
    x = int(input('введите первое число  '))
    y = int(input('введите второе число  '))
    z = int(input('введите третье число  '))
    d = sr(x, y, z)
    print('результат вычислений состовляет   ', d)
    print()

    vv = input("для выхода из программы введите stop или повторите расчеты")
print('работа программы завершена')
