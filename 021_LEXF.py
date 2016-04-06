import itertools

rosalind = open("rosalind_lexf.txt", "r")
file_input = rosalind.readlines()

alphabet = file_input[0].strip().split(" ")
k = file_input[1].strip()

results= itertools.product(alphabet, repeat = int(k))

for i in results:
    print "".join(i)
