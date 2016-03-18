bases = ["A", "C", "G", "T"]
bases_len = len(bases)
seq = "ACGCTGATCGTGTCATGCAT"
rev_comp = ""

for base in seq:
    rev_comp += bases[bases_len - 1 - bases.index(base)]

rev_comp = rev_comp[::-1]
print(rev_comp)
