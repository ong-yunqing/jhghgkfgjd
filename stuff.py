input_size = int(input())
lst = []
for i in range(input_size):
    temporary = int(input())
    lst.append(temporary)

def bubble_sort(data):
    swapped = True
    passes = len(lst) -1
    while swapped == True:
        swapped = False
        for i in range(passes-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                swapped = True
            passes = passes -1
    return data        
def merge (l1, l2):
    i = 0
    j = 0
    newl =[]
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            newl.append(l1[i])
            i +=1
        else:
            newl.append(l2[j])
            j +=1

    if i < len(l1):
        newl.extend(l1[:i])
    else:
        newl.extend(l2[:j])
    return newl