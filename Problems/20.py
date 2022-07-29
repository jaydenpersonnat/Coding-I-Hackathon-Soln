
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

print(sort2([5, {"hello" : 5, 3: 4, 7: 8, 9:2}, 3.7, 12,4, list(range(40))]))