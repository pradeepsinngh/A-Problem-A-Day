# Write a function reverse_complement(s) that returns the reverse complement of s.

def reverse_complement(seq):
    '''
    Returns the revers of the complement of given the string.

    Input: String
    Outpt: String
    '''

    alt_map = {'ins':'0'}
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

    for k,v in alt_map.items():
        seq = seq.replace(k,v)

    bases = list(seq)
    rev_seq = reversed([complement.get(base,base) for base in bases])
    rev_seq = ''.join(rev_seq)

    for k,v in alt_map.items():
        rev_seq = rev_seq.replace(v,k)

    return rev_seq
