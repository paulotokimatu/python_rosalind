rosalind = open("rosalind_long.txt", "r")
list_lines = rosalind.readlines()

n = -1
sequence = []

for i in list_lines:
    if ">" in i:
        n += 1
        temp = n
        sequence.append("")
    else:
        sequence[temp] += i.strip()

n = 0
switch = 0

while True:
    cat_strings = {}
    for i in range(0, len(sequence)): #Comparar a primeira com todas as outras
        if sequence[n] != sequence[i]:
            #Ver se tem strings overlapped
            for k in range(len(sequence[i])-1, len(sequence[i])/2,-1):
                if (k <= len(sequence[i])):
                    if (sequence[n][-k:] == sequence[i][:k]):
                        to_pop = i
                        cat_strings[to_pop] = sequence[n][:-k] + sequence[i]
                        #print sequence[n][-k:], sequence[i][:k], cat_strings[to_pop]
                        switch = 1
                        shortest = len(cat_strings[i])
                        break
                    elif (sequence[n][:k] == sequence[i][-k:]):
                        to_pop = i
                        cat_strings[to_pop] = sequence[n][k:] + sequence[i]
                        #print sequence[n][k:], sequence[i], cat_strings[to_pop]
                        switch = 1
                        shortest = len(cat_strings[i])
                        break
    #procurar pela menor cat_string
    if switch == 1:
        for i in cat_strings:
            if (shortest >= len(cat_strings[i])):
                shortest = len(cat_strings[i])
                temp = i
        sequence.pop(temp)
        sequence[0] = cat_strings[temp]
    if len(sequence) == 1:
        print sequence[0]
        break
    n = 0
    switch = 0
