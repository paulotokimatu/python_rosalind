def fib(n):
    if (n == 1 or n == 2):
        return 1
    else:
        return fib(n-2)*k + fib(n-1)

n = 30
k = 3

result = fib(n)
print result
