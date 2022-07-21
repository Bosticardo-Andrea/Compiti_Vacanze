def square_of_sum(number):
    x = (number*(number+1)//2)
    return x**2
def sum_of_squares(number):
    x = number*(number+1)
    x = x *(2*number+1)
    return x//6
def difference_of_squares(number):
    x = number*(number+1)
    x = x*(3*number**2-number-2)
    return x//12