file_input = open("rosalind_iev.txt", "r")

n_couples = file_input.read().split()
n_couples = map(int, n_couples)
prob_list = [2, 2, 2, 1.5, 1, 0]
n = 0
result = 0

for i in n_couples:
    result += i*prob_list[n]
    n += 1

print result
