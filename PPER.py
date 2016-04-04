import itertools

def factorial(number):
    n = 1
    for i in range(number, 0, -1):
        n *= i
    return n

rosalind = open("rosalind_pper.txt", "r")
number = rosalind.read().strip()

total, word = number.split()
total, word = int(total), int(word)

n = factorial(total)
k = factorial(total - word)

print (n/k) % 1000000
