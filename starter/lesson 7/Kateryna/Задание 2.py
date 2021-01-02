steps = 10

possibilities = [0, 1]
for i in range(2, steps+1):
    n1 = possibilities[i-1] + possibilities[i-2]
    possibilities.append(n1)

print('The amount of possibilities(in form of a list) to climb up the stairs with', steps, 'steps is equal to', possibilities, '.')