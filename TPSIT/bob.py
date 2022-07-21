def response(hey_bob):
    hey_bob = hey_bob.strip()
    if len(hey_bob) == 0:
        return "Fine. Be that way!"
    urla = hey_bob == hey_bob.upper() and hey_bob != hey_bob.lower()
    domanda = hey_bob[-1] == "?"
    if urla and domanda:
        return "Calm down, I know what I'm doing!"
    elif not urla and domanda:
        return "Sure."
    elif urla and not domanda:
        return "Whoa, chill out!"
    else:
        return 'Whatever.'