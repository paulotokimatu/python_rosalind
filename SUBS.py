import re

file_input = open("rosalind_subs(1).txt", "r")
sequence = file_input.readlines()

seq = sequence[0].strip()
pattern = sequence[1].strip()

for i in range(0,len(seq)-len(pattern)):
    if (seq[i:i+len(pattern)] == pattern):
        print i+1,


