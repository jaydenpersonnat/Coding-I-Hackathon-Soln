
def helper(element):
    if isinstance(element, str) or isinstance(element, list) or isinstance(element, set) or isinstance(element, dict):
        return len(element)
    elif element == True:
        return 0 
    elif element == False:
        return 1
    else:
        return element 

def sort2(lst): 
    lst.sort(key=helper)
    return lst

print(sort2([[1,2,3], 6, "hello world", 7.5, True, False]))