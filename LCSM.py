import re

def long_substr(data):
    substr = ""
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and is_substr(data[0][i:i+j], data):
                    substr = data[0][i:i+j]
    return substr

def is_substr(pattern, data):
    if len(data) < 1 and len(pattern) < 1:
        return False
    for i in range(len(data)):
        if pattern not in data[i]:
            return False
    return True


file_input = open("rosalind_lcsm.txt", "r")
lines = file_input.readlines()
sequence = []

for i in lines:
    if ">" in i:
        sequence.append("")
    else:
        sequence[-1] += i.strip()

print long_substr(sequence)
