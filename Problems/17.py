

def unzip(lst): 
    list1 = []
    list2 = []
    for item in lst: 
        list1.append(item[0])
        list2.append(item[1])
    
    return [list1, list2]

