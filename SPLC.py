import itertools

def translation(seq):
    aa = ""
    codon_list = [seq[i:i+3] for i in range(0, len(seq), 3)]
    for i in codon_list:
        if (table_code[i] == "Stop"):
            break
        aa += table_code[i]
    return aa

table_code = {"TTT": "F", "CTT": "L", "ATT": "I", "GTT": "V", "TTC": "F",
              "CTC": "L", "ATC": "I", "GTC": "V", "TTA": "L", "CTA": "L",
              "ATA": "I", "GTA": "V", "TTG": "L", "CTG": "L", "ATG": "M",
              "GTG": "V", "TCT": "S", "CCT": "P", "ACT": "T", "GCT": "A",
              "TCC": "S", "CCC": "P", "ACC": "T", "GCC": "A", "TCA": "S",
              "CCA": "P", "ACA": "T", "GCA": "A", "TCG": "S", "CCG": "P",
              "ACG": "T", "GCG": "A", "TAT": "Y", "CAT": "H", "AAT": "N",
              "GAT": "D", "TAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
              "TAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
              "TAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
              "TGT": "C", "CGT": "R", "AGT": "S", "GGT": "G", "TGC": "C",
              "CGC": "R", "AGC": "S", "GGC": "G", "TGA": "Stop",
              "CGA": "R", "AGA": "R", "GGA": "G", "TGG": "W", "CGG": "R",
              "AGG": "R", "GGG": "G" }

rosalind = open("rosalind_splc.txt", "r")
file_input = rosalind.readlines()

sequence = {}
n = -1

for i in file_input:
    if ">" in i:
        n += 1
        temp = i.strip()
        sequence[temp] = ""
    else:
        sequence[temp] += i.strip()
        if n == 0:
            gene = sequence[temp]

for i in sequence:
    if sequence[i] != gene:
        if sequence[i] in gene:
            gene = "".join(gene.split(sequence[i]))

print translation(gene)
