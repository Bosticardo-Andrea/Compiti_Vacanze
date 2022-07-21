def distance(strand1, strand2):
    if len(strand1) != len(strand2):
        raise ValueError("Strands must be of equal length.")
    c=0
    for x,y in zip(strand1, strand2):
        if x != y: c+=1
    return c