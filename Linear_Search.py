def linear_search(arr, target):
  for i in range(len(arr)):
    if arr[i] == target:
      return i
  return -1

example_array = [3, 5, 2, 4, 9]
target_value = 4
result = linear_search(example_array, target_value)
if result != -1:
  print(f"Element found at index: {result}")
else:
  print("Element not found in the array.")