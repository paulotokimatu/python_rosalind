# Print output in file

import itertools

rosalind = open("rosalind_lexv.txt", "r")
file_input = rosalind.readlines()

alphabet = file_input[0].strip().split(" ")
k = int(file_input[1].strip())

results_per_k ={}
words = {}

for i in range(1,k+1):
    results_per_k[i] = list(itertools.product(alphabet, repeat = i))
    words[i] = []
    for x in results_per_k[i]:
        words[i].append("".join(x))

def printing(letters, sufix):
    if letters == 1:
        for w in words[letters]:
            print w
            if letters+1 <= len(words):
                printing(letters+1, w)
    else:
        for w in words[letters]:
            if sufix == w[:letters-1]:
                print w
                if letters+1 <= len(words):
                    printing(letters+1, w)

printing(1,"")
