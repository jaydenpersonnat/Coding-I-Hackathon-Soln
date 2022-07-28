
from functools import reduce 

def add_digits(string):
    sum = 0 
    for char in string: 
        sum += int(char)

    return sum 

def luhn(card_number): 
    # Take card_number as an integer, convert it to a string, store each digit in a list
    # reverse the entire list
    card_number_lst = list(map(lambda char : int(char), str(card_number)))[::-1]
    sum = 0 
    double_index = 1 
    for index in range(len(card_number_lst)):
        if index == double_index: 
            sum += add_digits(str(2 * card_number_lst[index]))
            double_index += 2
        else:
               sum += card_number_lst[index]
        
    return sum % 10 == 0 

