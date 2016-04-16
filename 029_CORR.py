def revc(seq):
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    result = []
    for i in list(seq[::-1]):
        result.append(complement[i])
    return "".join(result)

def hamming(ref, query):
    n=0
    for a, b in zip(list(ref),list(query)):
        if (a != b):
            n += 1
    return n
    
rosalind = open("rosalind_test.txt", "r")
file_input = rosalind.readlines()

count_seq = {}
seq = {}

for line in file_input:
    if ">" in line:
        temp = line.strip()
        seq[temp] = ""
    else:
        seq[temp] += line.strip()

for x in seq:
    try:
        count_seq[revc(seq[x])] += 1
        count_seq[seq[x]] += 1
    except:
        count_seq[revc(seq[x])] = 1
        count_seq[seq[x]] = 1

seq_error = []
seq_ok = []

for x in seq:
    if count_seq[seq[x]] <= 1 and count_seq[revc(seq[x])] <= 1:
        seq_error.append(seq[x])
    else:
        seq_ok.append(seq[x])

for x in seq_error:
    for y in seq_ok:
        if hamming(y, x) == 1:
            print x + "->" + y
            break
        elif hamming(revc(y), x) == 1:
            print x + "->" + revc(y)
            break
