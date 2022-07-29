

def lettersum(string): 
    
    sum = 0 
    if string == "": 
        return 0 

    for char in string: 
        if char.isupper(): 
            sum += ord(char) - 64
        elif char.islower():
            sum += ord(char) - 96

    return sum


