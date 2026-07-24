
    




input_size = int(input())
choices = ["bubble","quick","insert","merge"]
lst = []
for i in range(input_size):
    temporary = int(input())
    lst.append(temporary)
choice = input("Choose your preferred method of sorting(bubble/quick/insert/merge): ")
if not choice.isalpha():
    return "idiot."
    choice = input("Choose your preferred method of sorting(bubble/quick/insert/merge): ")

elif choice not in choices:
    return "idiot."
    choice = input("Choose your preferred method of sorting(bubble/quick/insert/merge): ")
    
if choice == "bubble":
    bubble_sort(lst)

elif choice == "quick":
    quick_sort(lst)

elif choice == "insert":
    insertion_sort(lst)

elif choice == "merge":
    merge_sort(lst)



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

def merge_sort(data):
    if len(data) <= 1:
        return data
    else:
        mid = data//2
        l1 = data[:mid]
        l2 = data[mid:]
        sorted_l1 = merge_sort(l1)
        sorted_l2 = merge_sort(l2)
        return merge(sorted_l1,sorted_l2)
def insertion_sort(lst):
  for i in range(1, len(A)-1):
    curr = lst[i]
    pos = i
    while pos > 0 and lst[pos - 1] >= curr:
      lst[i] = lst[pos-1]
      pos -= 1

    lst[pos] = curr
