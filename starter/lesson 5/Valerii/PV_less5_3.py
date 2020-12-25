def plus(x, y):
    c = x + y
    return c

def min(x, y):
    c = x - y
    return c

def umn(x, y):
    c = x * y
    return c

def dl(x, y):
    c = x / y
    return c
print('программа выполняет операции +, -, *, /')
print('для завершения программы введите слово "stop" ')

d = ''  # строковой тип переменной
while d != 'stop':
    d = input("введите операцию, которую хотите совершить ")
    if d == '+' or d == '-' or d == '*' or d == "/":
        a = float(input('введите первое число '))
        b = float(input('введите второе число '))
        if d == '+':
            c = plus(a, b)
        elif d == '-':
            c = min(a, b)
        elif d == '*':
            c = umn(a, b)
        elif d == '/':
            if b == 0:
                print('недопустимый делитель')
                continue
            else:
                c = dl(a, b)
        print('результат вычисления ', c)

    elif d == "stop":
        break
    else:
        print('вы ввели некоректную операцию, повторите ввод операции или завершите работу')
print('работа программы завершена')
