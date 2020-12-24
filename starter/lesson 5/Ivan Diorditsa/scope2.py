def add(x):
    # nonlocal y
    y = -3

    def add2(a, b):
        # global y
        nonlocal y
        y = 10
        print(f'{y=}')
        global x
        x += 3
        return a + b

    print(f'before add2(): {y=}')
    ret = add2(x, 10)
    print(f'in function add(): {y=}')
    return ret


x = 1
y = -1
print(f'{x=}')
print(add(20))
print(f'{x=} {y=}')
print(add(30))
print(f'{x=} {y=}')
# print(add2(30, 30))
