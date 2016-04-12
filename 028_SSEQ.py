## To do: improve a lot the code

rosalind = open("rosalind_sseq.txt", "r")
file_input = rosalind.readlines()

sequence = {}
seq_name = []
result = []

for i in file_input:
    if ">" in i:
        temp = i.strip()
        seq_name.append(temp)
        sequence[temp] = ""
    else:
        sequence[temp] += i.strip()

n = 0
target = list(sequence[seq_name[0]])

for x in list(sequence[seq_name[1]]):
    while True:
        if n > len(target):
            break
        elif x == target[n]:
            if len(result) > 0:
                if n - result[-1] == 0:
                    n += 1
                    continue
            result.append(n+1)
            n += 1
            break
        else:
            if n <len(target)-1:
                n += 1
            else:
                break

print " ".join((map(str, result)))
