lst = [1, 2]  # packing
a, b = lst  # unpacking
print(a, b)


lst = [1, 2, 3, 4, 5]
# a, b = lst
first, *rest = lst  # pep-3132
print(first, rest)
x, y, *z = lst
print(x, y, z)


def add(x, y):
    return x + y


lst = [1, 2]
print(add(*lst))


def add2(*args):
    print(type(args))
    return args[0] + args[1]


print(add2(3, 4))


def add3(*args, param):
    return sum(args)


print(add3(1, 2, 3, 4, 5, 6, param=None))


def maxmax(*args):
    print(f'{len(args)=} {args=}')
    m = args[0]
    for i in args:
        if i > m:
            m = i
    return m


print(maxmax(10, 20, 30, 40, 50, 60, 70, 80))
print(maxmax(1))
print(maxmax(3, 4, 5))


def add3(x):
    print(f"{x=}")
    return x[0] + x[1]


print(add3((1, 2)))
