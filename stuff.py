def quicksort(lst):
    if not lst:
        return []
    equal_lst = []
    less_than = []
    greater_than = []
    equal = lst[len(lst)//2]
    for num in lst:
        if num < equal:
            less_than.append(num)
        elif num > equal:
            greater_than.append(num)
        else:
            equal_lst.append(num)
    result = quicksort(less_than) + equal_lst + quicksort(greater_than)
    return result       
          
    
