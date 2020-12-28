# no recursion
def nat_num(x):
    for a in range(1, x+1):
        global n
        n += a
    return n

n = 0
print(nat_num(5))

# recursion
def recurs(n):
    res = 0
    if n > 0:
        res += n
        recurs(n-1)
    return res

print(recurs(n))