a = int(input('введите целое число а'))
b = int(input('введите целое число b, большее чем а'))
while a >= b:
    print('вы ввели неправильное число b')
    b = int(input('введите целое число b, большее чем а'))
c = a
while c < b:
    c = c + 1
    a = a + c

print(a)
