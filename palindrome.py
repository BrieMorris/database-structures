def is_palindrome(s):
  left, right = 0, len(s) - 1

  while left < right:
    # skip non-alphanumeric characters (optional, based on definition of palindrome)
    while left < right and not s[left].isalnum():
      left += 1
    while left < right and not s[right].isalnum():
      right -= 1

    # compare characters
    if s[left].lower() != s[right].lower():
      return False
    
    # Move pointers towards the center 
    left += 1
    right -= 1

  return True

# Example usage 
string = "A man, a plan, a canal, Panama"
print(is_palindrome(string)) # should return true