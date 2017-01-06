from random import randint

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

class MyException(Exception):
  pass

test_cases = []
for i in range(0, 5):
  li = [randint(0, 100) for a in range(0, randint(0, 1000))]
  test_cases.append(li)
test_cases.append([])

for li in test_cases:
  if counting_sort(li, 100) == sorted(li):
    print ("The couting sort algorithm is correct!")  
  else:
    raise MyException("The counting sort algorithm is incorrect!")
    
