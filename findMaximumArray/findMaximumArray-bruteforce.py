def max_subarray(A):
  max_sum = float("-inf")
  left = right = -1 
  for i in range(0, len(A)):
    max_array_sum = max_sum_local = A[i]
    new_left = new_right = i
    for j in range(i+1, len(A)):
      max_array_sum += A[j]
      if max_array_sum > max_sum_local:
        max_sum_local = max_array_sum
	new_right = j
    if max_sum_local > max_sum:
       max_sum = max_sum_local
       left = new_left
       right = new_right
  return max_sum, left, right

     
