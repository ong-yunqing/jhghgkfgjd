def quicksort(lst):
    if not lst:
        return []
    equal_lst = []
    equal = lst[len(lst)//2]
    less_than = []
    greater_equal = []
    for num in lst:
        if num < equal:
            less_than.append(num)
        elif num > equal:
            greater_equal.append(num)
        else:
            equal_lst.append(num)
    result = quicksort(less_than) + equal_lst + quicksort(greater_equal)
    return result       
          
    
