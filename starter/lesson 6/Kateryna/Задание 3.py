def count(steps):
    if steps == 0:
        return 0
    elif steps == 1:
        global chances
        return 1
    else:
        return count(steps-1) + count(steps-2)

stairs = 10

print('The amount of possibilities to climb up the stairs with', stairs, 'steps is equal to', count(10), '.')