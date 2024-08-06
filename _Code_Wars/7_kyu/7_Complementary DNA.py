pairs = {'A':'T','T':'A','C':'G','G':'C'}
def DNA_strand(dna):
    return ''.join([pairs[x] for x in dna])


print(DNA_strand("AAAA"), "TTTT", "String AAAA is")
print(DNA_strand("ATTGC"), "TAACG", "String ATTGC is")
print(DNA_strand("GTAT"), "CATA", "String GTAT is")


def DNA_strand(dna):
    dct = {'T': 'A', 'A': 'T', 'C': 'G', 'G': 'C',}

    res = ''
    for c in dna:
        for key, value in dct.items():
            if key == c:
                res += value

    return res