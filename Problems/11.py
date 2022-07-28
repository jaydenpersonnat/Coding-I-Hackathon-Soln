import sys

def tax(income): 

    total_tax = 0 

    brackets = [10000, 30000, 100000, sys.maxsize]
    percentage = [0.0, 0.10, 0.25, 0.40]

    for index in range(len(brackets)):
        if index == 0 and income >= brackets[index]: 
            total_tax += brackets[index] * percentage[index]
            income -= brackets[index]
        elif index == 0 and income <= brackets[index]: 
            total_tax += income * percentage[index]
            break
        elif income >= (brackets[index] - brackets[index - 1]): 
            total_tax += (brackets[index] - brackets[index - 1]) * percentage[index]
            income -= (brackets[index] - brackets[index - 1])
        else: 
            total_tax += income * percentage[index]
            break 

    return format(total_tax, '.2f')

