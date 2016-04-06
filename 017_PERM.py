import itertools
rosalind = open("rosalind_perm.txt", "r")
number = rosalind.read().strip()

list_numbers = range(1,int(number)+1)
result = list(itertools.permutations(list_numbers))

print len(result)
for i in range(len(result)):
    for x in result[i]:
        print x,
    print ""
