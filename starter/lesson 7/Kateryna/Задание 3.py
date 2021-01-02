prime_num = []
amount = 125
for candidate in range(2, amount+1):
    test = True
    for x in range(2, candidate):
        if candidate % x == 0:
            test = False
    if test == True:
        prime_num.append(candidate)

print(prime_num)