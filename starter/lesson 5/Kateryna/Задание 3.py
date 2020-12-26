def div(a=2, b=1):
    if b != 0:
        res = a/b
        return res
    else:
        print('No division with 0 allowed!')

def sum(a, b):
    res = a + b
    return res

def subt(a, b):
    return a - b

def mult(a, b):
    return a * b

op = ''
while op != 'stop':
    op = input('Please enter an operation ')
    a = int(input('Enter your first number '))
    b = int(input('Enter your second number '))
    if op == '/':
        print(div(a, b))

    elif op == '+':
        print(sum(a, b))

    elif op == '-':
        print(subt(a, b))

    elif op == '*':
        print(mult(a, b))

else:
    print('The program is shutting down.')



