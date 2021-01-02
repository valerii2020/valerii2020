import functools
import time


@functools.lru_cache(maxsize=1000)
def fib(n):
    global calls
    calls += 1

    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-2) - fib(n-1)


n = 900
calls = 0
start = time.time()
r = fib(n)
end = time.time()
print(f'{n=} {r=} {calls=} {end-start=}')
