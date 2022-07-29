import sys 

def largest(lst): 
    converted_lst = [] 
    for element in lst: 
        if isinstance(element, str) or isinstance(element, list) or isinstance(element, set) or isinstance(element, dict):
            converted_lst.append(len(element))
        elif element == True:
            converted_lst.append(0)
        elif element == False:
            converted_lst.append(1) 
        else:
            converted_lst.append(element)
       
    largest = 1 - sys.maxsize
    index_of_element = None 
    for index in range(len(converted_lst)): 
        if converted_lst[index] > largest:
            largest = converted_lst[index]
            index_of_element = index 

    return lst[index_of_element]

