COMPLEMENTS = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U'
}
def to_rna(sequence):
    try:
        return ''.join(COMPLEMENTS[x] for x in sequence)
    except KeyError as e:
        return ''