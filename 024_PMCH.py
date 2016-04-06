def factorial(n):
    x = 1
    for i in range(n, 0, -1):
        x *= i
    return x

rosalind = open("rosalind_pmch.txt", "r")
file_lines = rosalind.readlines()

sequence = {}

for i in file_lines:
    if ">" in i:
        temp = i.strip()
        sequence[temp] = ""
    else:
        sequence[temp] += i.strip()

AU = []
CG = []

for i in list(sequence[temp]):
    if i == "A" or i == "U":
        AU.append(i)
    if i == "C" or i == "G":
        CG.append(i)

print factorial(len(AU)/2) * factorial(len(CG)/2)
