import itertools

rosalind = open("rosalind_kmer.txt", "r")
file_input = rosalind.readlines()

seq = {}
k = 4

for i in file_input:
    if ">" in i:
        temp = i.strip()
        seq[temp] = ""
    else:
        seq[temp] += i.strip()

kmer = list(itertools.product("ACTG", repeat=4))
sorted_kmer = []
n_kmer = {}

for i in kmer:
    sorted_kmer.append("".join(i))
    n_kmer["".join(i)] = 0

sorted_kmer.sort()

for i in range(0, len(seq[temp])-k+1):
    n_kmer[seq[temp][i:i+k]] += 1

for n in sorted_kmer:
    print n_kmer[n],
