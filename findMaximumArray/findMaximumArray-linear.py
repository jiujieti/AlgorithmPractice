def max_subarray(A):
  max_ending_here = max_sum = A[0]
  left = right = 0
  new_left = 0
  for i in range(1, len(A)):
    if A[i] > max_ending_here + A[i]:
      new_left = i
      max_ending_here = A[i]
    else:
      max_ending_here += A[i] 
    if max_sum < max_ending_here:   
      max_sum = max_ending_here
      left = new_left
      right = i
  return max_sum, left, right

