# To do: use property of logarithms in the hint

import math

def calc_prob(prob_cg, prob_at):
    prob = 1
    for nuc in list(sequence):
        if nuc == "A" or nuc == "T":
            prob *= prob_at
        elif nuc == "C" or nuc == "G":
            prob *= prob_cg
    return prob

rosalind = open("rosalind_prob.txt", "r")
file_lines = rosalind.readlines()

sequence = file_lines[0].strip()
prob_list = file_lines[1].strip().split()

for i in prob_list:
    prob_cg = float(i)/2
    prob_at = (1-float(i))/2
    print ("%.3f" % math.log(calc_prob(prob_cg, prob_at), 10)),
