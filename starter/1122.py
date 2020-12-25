def add(x, y):
    res = x + y
    return res


def add2(x):
    res = add(x, 10)
    return res


print(add2(20))