def is_isogram(s):
    lettere = [c.lower() for c in s if c.isalpha()]
    return len(set(lettere)) == len(lettere)