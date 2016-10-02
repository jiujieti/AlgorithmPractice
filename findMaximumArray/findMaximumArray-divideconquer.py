def mid_crossing_subarray(A, low, high):
  left_sum = right_sum  =  0
  max_left_sum = max_right_sum = float("-inf")
  mid = (high - low) / 2 + low
  left = right = -1
  for i in range(mid, low):
    left_sum += A[i]
    if left_sum > max_left_sum:
      max_left_sum = left_sum
      left = i
  for j in range(mid+1, high):
    right_sum += A[j]
    if right_sum > max_right_sum:
      max_right_sum = right_sum
      right = j
  return max_left_sum + max_right_sum, left, right

def max_subarray(A, low, high):
  if low == high:
     return A[low], low, high
  mid = (high - low) / 2 + low
  left_sum, left_left, left_right = max_subarray(A, low, mid)
  right_sum, right_left, right_right = max_subarray(A, mid + 1, high)
  mid_crossing_sum, mid_left, mid_right = mid_crossing_subarray(A, low, high)
  if left_sum >= right_sum and left_sum >= mid_crossing_sum:
    return left_sum, left_left, left_right
  elif right_sum >= left_sum and right_sum >= mid_crossing_sum:
    return right_sum, right_left, right_right
  else:
    return mid_crossing_sum, mid_left, mid_right

