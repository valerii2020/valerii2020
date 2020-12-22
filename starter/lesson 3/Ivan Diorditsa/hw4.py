import math

op = input("введите операцию: ")

if op == 'tan':
    x = input("введите х (в градусах): ")
    x = int(x)
    rad = math.radians(x)
    print(f"{math.tan(rad)=}")
