rosalind = open("rosalind_tran.txt", "r")
file_input = rosalind.readlines()

sequence = {}
name_seq = []

for i in file_input:
    if ">" in i:
        temp = i.strip()
        name_seq.append(temp)
        sequence[temp] = ""
    else:
        sequence[temp] += i.strip()

transition = float(0)
transversion = float(0)

for a, b in zip(list(sequence[name_seq[0]]), list(sequence[name_seq[1]])):
    if a != b:
        if a in ["A", "G"] and b in ["C", "T"]:
            transversion += 1
        elif a in ["C", "T"] and b in ["A", "G"]:
            transversion += 1
        else:
            transition += 1
            
print transition/transversion
