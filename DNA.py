file = open("rosalind_dna.txt", "r")
x = file.read()

list_nuc = list(x)
counter = {}

for i in x:
    counter[i] = 0

for i in x:
    counter[i] += 1
    
print counter["A"], counter["C"], counter["G"], counter["T"]
