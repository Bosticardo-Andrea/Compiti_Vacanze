def is_armstrong_number(number):
    n = len(str(number))
    totale = 0
    for digit in str(number):
        totale = totale + (int(digit) ** n)
    return totale == number