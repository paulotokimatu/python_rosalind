file_input = open("rosalind_hamm.txt", "r")
sequence = file_input.readlines()

seq1 = list(sequence[0].strip())
seq2 = list(sequence[1].strip())

n=0

for a, b in zip(seq1,seq2):
    if (a != b):
        n += 1

print n
