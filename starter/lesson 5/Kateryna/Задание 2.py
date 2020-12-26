def calc_float(start=-5.5, stop=5, step=0.5):
    op = input('Please enter an operation, sq or div2? ')
    while start < stop:
        if op == 'sq':
            print(sq(start))
        elif op == 'div2':
            print(div2(start))
        start += step

def sq(numb):
    return (numb ** 2)

def div2(numb):
    return (numb / 2)
start = - 5.5
op = ''
calc_float()