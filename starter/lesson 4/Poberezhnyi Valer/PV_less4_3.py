x = int(input('ведите высоту прямоугольного треугольника '))
y = int(input('ведите ширину прямоугольного треугольника '))
p = 0
for i in range(x):
    while p < y:
        p = p + 1 # счетчик символов в строке
        for i in range(p):
            print('*', end='')  # выполнение одной внутренней итерации в строку
        print()  # переход на следующую строку