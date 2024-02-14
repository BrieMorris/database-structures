def sum_numbers(n):
  if n<= 1: #Base case
    return n
  else: #recursive case 
    return n + sum_numbers(n-1)
  
def sum_numbers_tail_recursive(n, accumulator=0):
  if n <= 0: # adjusted base case
    return accumulator
  else: 
    return sum_numbers_tail_recursive(n - 1, accumulator + n)