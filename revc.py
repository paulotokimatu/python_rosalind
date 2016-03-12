file = open("rosalind_revc(1).txt", "r")
x = file.read()

x = x[::-1]
list_nuc = list(x)

def complement(original):
    if (original == "A"):
        return "T"
    elif (original == "C"):
        return "G"
    elif (original == "G"):
        return "C"
    elif (original == "T"):
        return "A"

for i in range(0,len(x)):
    list_nuc[i] = complement(list_nuc[i])

print list_nuc
print "".join(list_nuc)
