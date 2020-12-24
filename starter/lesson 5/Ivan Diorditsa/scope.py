def add(a):
    y = 100  # локальная
    print(f'inside function add: {id(y)=}')
    return a + y


# print(add(10, 20), add(1, 2), add(a=-1, b=-2))
print(add(10))
# print(b)

# scope


def add2(x):
    # local scope
    # y = 10  # локальная переменная
    global y
    print(f'inside function add2 {id(y)=}')
    return x + y


# global scope
y = 5  # глобальная переменная
print(f'{add2(3)=}')
print(f'{id(y)=} {y=}')
