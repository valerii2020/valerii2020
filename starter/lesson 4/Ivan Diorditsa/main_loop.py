import math

op = ''
i = 0
while op != 'q':
    i += 1
    op = input(f"{i=} введите операцию (tan, q для выхода): ")

    if op == '':
        continue

    if op == 'tan':
        x = input("введите х (в градусах): ")
        x = int(x)
        rad = math.radians(x)
        print(math.tan(rad))
    elif op == 'q':
        break
else:
    print("мы в else блоке цикла")

print("вышли из цикла")