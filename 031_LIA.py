import itertools
from math import factorial

def combination(x, y):
    return factorial(x)/(factorial(y)*factorial(x-y))
    
rosalind = open("rosalind_lia.txt", "r")
file_input = rosalind.read()
parameters = file_input.split()
k = int(parameters[0])
N = int(parameters[1])

yes = 0.25
no = 1 - yes
n_children = 2 ** k


comp_result = 0

for i in range(N):
    comp_result += combination(n_children, i) * (yes ** i) *    (no ** (n_children-i))

print round(1-comp_result,3)
