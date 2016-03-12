file = open("rosalind_rna.txt", "r")
x = file.read()

list_nuc = list(x)

for i in range(0,len(x)):
    if (list_nuc[i] == "T"):
        list_nuc[i] = "U"

print "".join(list_nuc)
