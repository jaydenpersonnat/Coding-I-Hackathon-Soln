
 

def sum_numerals(roman_numeral):
    sum = 0 
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    for char in roman_numeral:
        sum += roman[char]

    # Remove overcounted values - IV, IX, etc...
    for index in range(len(roman_numeral)):
        if index > 0 and roman[roman_numeral[index - 1]] < roman[roman_numeral[index]]:
            sum -= (2 * roman[roman_numeral[index - 1]])

    return sum 

def numcompare(numeral_one, numeral_two): 
    return sum_numerals(numeral_one) < sum_numerals(numeral_two)

