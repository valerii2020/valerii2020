def foo(x):
    x = 20
    print('local', x)


x = 10
foo(x)
print('global', x)


def bar(x):
    # x = [1, 2, 3]
    x.clear()
    x.append(3)
    x.append(2)
    x.append(1)
    print(f"3 {id(x)=}")
    print("local", x)


x = ['мама', 'мыла', "раму"]
print(f"1 {id(x)=}")
bar(x)
print(f"2 {id(x)=}")
print("global", x)
