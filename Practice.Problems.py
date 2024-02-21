# Target sum  from array

def twoSum(nums, target):
  #Create a dictionary to store the value and its index
  hashmap = {}
  # Iterate through the array
  for i, num in enumerate(nums):
    complement = target - num
    if complement in hashmap:
      #If the complement is found, return the indices
      return[hashmap[complement], i]
    #Stor the number and its index in the hashmap
    hashmap[num] = i
  return []