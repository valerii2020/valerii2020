import math

while True:
    op = ''
    while op != 'tan' and op != '+' and op != 'q':
        op = input("введите операцию (tan или +): ")

    if op == 'q':
        break

    if op == 'tan':
        x = input("введите х (в градусах): ")
        x = int(x)
        rad = math.radians(x)
        print(math.tan(rad))