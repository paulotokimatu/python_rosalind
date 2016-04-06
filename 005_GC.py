import re

def calc_gc(sequence):
    n = 0
    seq = list(sequence)
    for n_nuc in seq:
        if (n_nuc == "G" or n_nuc == "C"):
            n += 1
    return n
#    return 100*float(n)/len(sequence)

fasta = open("rosalind_gc.txt", "r")

list_lines = fasta.readlines()

gc_content = {}
seq_len = {}
name_seq = ""
max_gc_number = 0
max_gc_name = ""

for i in list_lines:
    if re.search(">", i) :
        name_seq = i.strip()
        gc_content[name_seq] = 0
        seq_len[name_seq] = 0
    else:
        gc_content[name_seq] += calc_gc(i.strip())
        seq_len[name_seq] += len(i.strip())

for key, value in gc_content.iteritems():
    value = float(value)*100/seq_len[key]
    if (value > max_gc_number):
        max_gc_number = value
        max_gc_name = key

print max_gc_name, "\n", max_gc_number
