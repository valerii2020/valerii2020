def add(arg1=0, arg2=0):
    print(f'{id(arg1)=} {id(arg2)=}')
    res = arg1 + arg2
    print(f'{id(res)=}')
    return res


x = input("введите х: ")
x = int(x)
y = input("введите y: ")
y = int(y)

print(f'{id(x)=} {id(y)=}')
D = add(arg2=x, arg1=y)
print(f'{id(D)=}')
print(D)
