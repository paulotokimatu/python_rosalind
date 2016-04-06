import itertools

rosalind = open("rosalind_sign.txt", "r")
number = int(rosalind.read().strip())

output_file = open("output3.txt", "w")

list_numbers = []

for n in range(1, number+1):
    list_numbers.append(n)
    list_numbers.append(-n)

all_perm = list(itertools.permutations(list_numbers, number))
perm_final = []

for seq in all_perm:
    switch = 0
    for x in range(0, len(seq)-1):
        for ref in range (x, len(seq)):
            if seq[x] == seq[ref]*-1:
                switch = 1
    if switch == 0:
        perm_final.append(seq)

output_file.write(str(len(perm_final)))
output_file.write("\n")

for result in perm_final:
    output_file.write(str(" ".join(map(str, result))))
    output_file.write("\n")

output_file.close()
