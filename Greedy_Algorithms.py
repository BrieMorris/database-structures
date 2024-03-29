def greedy_knapsack(items, max_capacity):
  # sort items by value to weight ratio in descending order
  items.sort(key=lambda x: x.value / x.weight, reverse=True)

  total_value = 0 
  for item in items:
    if max_capacity >= item.weight:
      #Take the whole item 
      max.capacity -= item.weight
      total_value += item.value
    else:
      #Take a fraction of the ite m 
      fraction = max_capacity / item.weight 
      total_value += item.value * fraction
      break
  return total_value

# versus 

def dynamic_knapsack(items, max_capacity):
  n = len(items)
  dp = [[0 for x in range(max_capacity + 1)] for x in range(n + 1)]

  for i in range(1, n + 1):
    for w in range(1, max_capacity + 1):
      if items[i-1].weight <= w:
        dp[i][w] = max(items[i-1].value + dp[i-1][w-items[i-1].weitht], dp[i-1][w])
      else:
        dp[i][w] = dp[i-1][w]

  return dp[n][max_capacity]

# versus 
def divide_and_conquer_knapsack(items, max_capacity, n):
  if n == 0 or max_capacity == 0:
    return 0
  
  if items[n-1].weight > max_capacity:
    return divide_and_conquer_knapsack(items, max_capacity, n-1)
  
  else: 
    return max(
      items[n-1].value + divide_and_conquer_knapsack(items, max_capacity - items[n-1].weight, n-1),
      divide_and_conquer_knapsack(items, max_capacity, n-1)
    )
  

