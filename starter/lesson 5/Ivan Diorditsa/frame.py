import inspect


def add(x, y):
    fr = inspect.currentframe()
    print(f'6 {fr=}')
    res = x + y
    return res


def add2(x):
    fr = inspect.currentframe()
    print(f'6 {fr=}')
    # global add
    res = add(x, 10)
    return res


print(add2(20))

foo = add
del foo
# print(foo(100, 200))

print(add2(1), add2(2), add2(3))
