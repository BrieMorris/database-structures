def bubble_sort(arr):
  n = len(arr)
  # Traverse through all array elements
  for i in range(n):
    # last i elements are already in place 
    for j in range(0, n-i-1):           # traverse the array from 0 to n-i-1
      #swap if the element founf is greater that the next element
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr

sample_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(sample_list)
print(sorted_list)