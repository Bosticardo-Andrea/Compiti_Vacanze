def classify(number):
    if number <= 0:
        raise ValueError('Classification is only possible for positive integers.') 
    s = 0
    for i in range(1, number):
        if number % i == 0: s += i
    if s == number: return 'perfect'
    if s > number:return 'abundant'
    return 'deficient'