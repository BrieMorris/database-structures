def quick_sort(arr):
  if len(arr) <= 1:
    return arr
  else:
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x> pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)
  

arr = [29, 10, 14, 37, 13,]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)

