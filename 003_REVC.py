rosalind = open("rosalind_revc.txt", "r")
x = rosalind.read().strip()

result = []
complement = {"A": "T", "T": "A", "C": "G", "G": "C"}

for i in list(x[::-1]):
    result.append(complement[i])

print "".join(result)
