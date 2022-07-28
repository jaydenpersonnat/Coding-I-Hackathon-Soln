

def zip(list1, list2): 

    if len(list1) == 0 and len(list2) == 0: 
        return [] 
    else: 
        return [[list1[0], list2[0]]] + zip(list1[1: ], list2[1: ])

