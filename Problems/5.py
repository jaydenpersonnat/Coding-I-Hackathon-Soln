

def common(list1, list2):
    return list(set(list1).intersection(set(list2)))


print(common([2,3,-5,6,7,3,3,2], [1,5,8,4,6,3,2,3,1]))