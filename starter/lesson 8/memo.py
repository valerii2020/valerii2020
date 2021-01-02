import time

cache = [1, 1]


def fib(n):
    global calls
    calls += 1

    if cache[n] is None:  # cache miss
        if cache[n-1] is None:
            cache[n-1] = fib(n-1)

        if cache[n-2] is None:
            cache[n-2] = fib(n-2)

        cache[n] = cache[n-1] + cache[n-2]

    return cache[n]


for i in range(900, 901):
    calls = 0
    while len(cache) < i+1:
        cache.append(None)
    t = time.time()
    r = fib(i)
    print(f'{i=} {r=} {calls=} {time.time()-t=}')
