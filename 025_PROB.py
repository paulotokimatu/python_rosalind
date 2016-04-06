import math

def calc_prob(prob_cg, prob_at):
    prob = 0
    for nuc in list(sequence):
        if nuc == "A" or nuc == "T":
            prob += math.log(prob_at, 10)
        elif nuc == "C" or nuc == "G":
            prob += math.log(prob_cg, 10)
    return prob

rosalind = open("rosalind_prob.txt", "r")
file_lines = rosalind.readlines()

sequence = file_lines[0].strip()
prob_list = file_lines[1].strip().split()

for i in prob_list:
    prob_cg = float(i)/2
    prob_at = (1-float(i))/2
    print ("%.3f" % calc_prob(prob_cg, prob_at)),
