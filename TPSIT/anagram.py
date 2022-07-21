def find_anagrams(word, candidates):
    lista = []
    for x in candidates:
        if x.casefold() != word.casefold() and sorted(x.casefold()) == sorted(word.casefold()):
            lista.append(x)
    return lista