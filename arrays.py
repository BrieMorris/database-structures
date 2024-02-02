from array import array

arr = array('i', [1, 2, 3, 4, 5])

print(arr[0]) # Output: 1
print(arr[2]) # Output: 3

arr1 = ('i', [1, 2, 3])
arr1.append(4) # Adds 4 to the end
arr1.extend([5, 6]) # Adds 5 & 6 to the end
arr1.pop() # removes the last elelment, 6 inthis case


# using the loop 
for element in arr1:
  print(element)

# Using while loop
counter = 0 
condition = True
while condition:
  print(arr1[counter])
  counter += 1
  if counter >= len(arr1):
    condition = False