from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_cached(num):
    if n <= 1:
        return n
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)

print(fibonacci_cached(num))
