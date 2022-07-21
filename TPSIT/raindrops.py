def convert(number):
    el = {
        3: 'Pling',
        5: 'Plang',
        7: 'Plong',
    }
    suono = ""
    for k, v in el.items():
        if number % k == 0:
            suono += v
    return suono or str(number)