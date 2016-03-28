import re

def revc(pattern):
    temp = ""
    for nuc in pattern:
        temp += complement[nuc]
    temp = "".join(temp)
    return temp[::-1]

rosalind = open("rosalind_revp.txt", "r")
file_input = rosalind.readlines()

complement = {"A": "T", "C": "G", "G": "C", "T": "A"}
seq = {}

for i in file_input:
    if ">" in i:
        temp = i.strip()
        seq[temp] = ""
    else:
        seq[temp] += i.strip()

for key in seq:
    for k in range(4, 13):
        for i in range(0, len(seq[key])-k+1):
            pattern = revc(list(seq[key][i:i+k]))
            if seq[key][i:i+k] == pattern:
                print i+1, k
            
