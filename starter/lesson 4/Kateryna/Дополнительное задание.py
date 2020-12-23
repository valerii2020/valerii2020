a = input('Hight of the rectangle?')
b = input('Length of the rectangle')

a = int(a)
b = int(b)

for x in range(1, a+1):
    for y in range(1, b+1):
        print('*', end="")

    print('')
