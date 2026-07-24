def insertion_sort(lst):
  for i in range(1, len(A)-1):
    curr = lst[i]
    pos = i
    while pos > 0 and lst[pos - 1] >= curr:
      lst[i] = lst[pos-1]
      pos -= 1

    lst[pos] = curr
    

insertion_sort([4,2,4,5,10,3])



