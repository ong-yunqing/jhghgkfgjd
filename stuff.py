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
            