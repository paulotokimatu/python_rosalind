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

def translation(helper, seq):
    temp = ""
    while True:
        if ( helper + 3 > len(sequence)):
            return
        if (table_code[seq[helper:helper+3]] == "Stop"):
            candidate_prot[temp] = ""
            return
        else:
            temp += table_code[seq[helper:helper+3]]
        helper += 3

def setting_frame(seq):
    for k in range(0,3):
        helper = k
        while True:
            if (seq[helper:helper+3] == "ATG"):
                translation(helper, seq)
            if ( helper + 3 > len(seq)):
                break
            else:
                helper += 3
            
rosalind = open("rosalind_orf.txt", "r")
sequence = ""
candidate_prot = {}

for i in rosalind.readlines():
    if ">" not in i:
        sequence += i.strip()

sequence = list(sequence)

# Making reverse complement sequence
dict_complement = {"A":"T", "T":"A", "C":"G", "G":"C",}
complement = []
for i in sequence:
    complement.append(dict_complement[i])

complement_seq = "".join(complement)[::-1]
sequence = "".join(sequence)

setting_frame(sequence)
setting_frame(complement_seq)

for prot in candidate_prot:
    print prot
