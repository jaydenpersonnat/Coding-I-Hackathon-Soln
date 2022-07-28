
def digit_sum(number): 
    sum = 0 
    for digit in number: 
        sum += int(digit)

    return str(sum)

def additive_persistence(number): 

    counter = 1 

    if len(str(number)) == 1:
        counter = 0 
    else: 
        while len(digit_sum(str(number))) > 1: 
            number = digit_sum(str(number))
            counter += 1

    return counter

print(additive_persistence(1468))