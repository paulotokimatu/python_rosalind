# To do: Use numpy to create a matrix

import re

fasta = open("rosalind_cons(1).txt", "r")
list_lines = fasta.readlines()

name_seq = ""
sequence = {}

for i in list_lines:
    if re.search(">", i):
        name_seq = i.strip()
        sequence[name_seq] = ""
    else:
        sequence[name_seq] += i.strip()

A = [0]*len(sequence[name_seq])
C = [0]*len(sequence[name_seq])
G = [0]*len(sequence[name_seq])
T = [0]*len(sequence[name_seq])
list_consensus = [""]*len(sequence[name_seq])

for key, value in sequence.iteritems():
    n = 0
    for i in list(value):
        if (i == "A"):
            A[n] += 1
        elif (i == "C"):
            C[n] += 1
        elif (i == "G"):
            G[n] += 1
        elif (i == "T"):
            T[n] += 1
        n += 1

for i in range(0,len(sequence[name_seq])):
    if (max(A[i], C[i], G[i], T[i]) == A[i]):
        list_consensus[i] = "A"
    elif (max(A[i], C[i], G[i], T[i]) == C[i]):
        list_consensus[i] = "C"
    elif (max(A[i], C[i], G[i], T[i]) == G[i]):
        list_consensus[i] = "G"
    elif (max(A[i], C[i], G[i], T[i]) == T[i]):
        list_consensus[i] = "T"
    
print "".join(list_consensus)
print "A:", " ".join(map(str, A))
print "C:", " ".join(map(str, C))
print "G:", " ".join(map(str, G))
print "T:", " ".join(map(str, T))
