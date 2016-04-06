import re

fasta = open("rosalind_grph(1).txt", "r")
list_lines = fasta.readlines()

name_index = []
sequence = {}
k = 3
n = -1

for i in list_lines:
    if re.search(">", i):
        n += 1
        temp_name = i.strip()
        name_index.append(temp_name[1:])
        sequence[name_index[n]] = ""
    else:
        sequence[name_index[n]] += i.strip()

for i in range(0,n+1):
    for x in range(i+1,n+1):
        temp1 = sequence[name_index[i]]
        temp2 = sequence[name_index[x]]
        if (temp1 == temp2):
            next
        if (temp1[-k:] == temp2[0:k]):
            print name_index[i], name_index[x]
        if (temp1[0:k] == temp2[-k:]):
            print name_index[x], name_index[i]
            
