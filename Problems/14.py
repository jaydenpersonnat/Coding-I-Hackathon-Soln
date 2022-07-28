

def shiftRight(string, num): 
    
    tmp = [char for char in string] 

    for index in range(len(string)): 
        tmp[(index + num) % len(string)] = string[index]

    return "".join(tmp)



