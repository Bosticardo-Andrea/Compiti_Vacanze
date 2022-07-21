def is_pangram(word):
    alfabeto = set('abcdefghijklmnopqrstuvwxyz')
    carattere = set(word.lower())
    return not (alfabeto - carattere)