def memoize(f):
    cache = {}
    def helper(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return helper
    
@memoize
def fib(n):
    if (n == 1 or n == 2):
        return 1
    else:
        return fib(n-2)*k + fib(n-1)

n = 40
k = 3

result = fib(n)
print result
