def counting_sort(li, k):
  c = [0] * (k+1)
  for j in range(0, len(li)):
    c[li[j]] += 1
  for i in range(1, k+1):
    c[i] += c[i-1]  
  res = [0] * len(li)
  for j in range(len(li)-1, -1, -1):
    res[c[li[j]] - 1] = li[j]
    c[li[j]] -= 1
  return res

