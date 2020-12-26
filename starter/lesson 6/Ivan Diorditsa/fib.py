
def fib(index):
    all_numbers = [0, 1]

    for i in range(2, index+1):
        number = all_numbers[i-1] + all_numbers[i-2]
        all_numbers.append(number)

    return all_numbers[index]


# for i in range(10):
#     print(fib(i))


def fib_recurs(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        return fib_recurs(index-1) + fib_recurs(index-2)


for i in range(10):
    print(fib_recurs(i))
