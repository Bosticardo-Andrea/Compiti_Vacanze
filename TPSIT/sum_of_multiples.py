def sum_of_multiples(limit, values):
    multipli = []
    for val in values:
        if val > 0:
            for multiple in range(val,limit,val):
                multipli.append(multiple)
    multipli = set(multipli) #rimuovere i doppioni
    print(multipli)
    return sum(multipli)