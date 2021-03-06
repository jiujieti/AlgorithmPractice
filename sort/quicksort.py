from random import randint

def partition(li, p, r):
  pivot = li[r]
  i = p
  for j in range(p, r):
    if li[j] <= pivot:
      li[i], li[j] = li[j], li[i]
      i += 1
  li[i], li[r] = li[r], li[i]
  return i
 

def quicksort(li, p, r):
  if p < r:
    q = partition(li, p, r)
    quicksort(li, p, q-1)
    quicksort(li, q+1, r)
  return li

tests = []
for i in range(0, 5):
  li = [randint(-100, 100) for j in range(0, randint(0, 1000))]
  tests.append(li)
tests.append([])

for li in tests:
  li_bak = li.copy()
  if sorted(li_bak) == quicksort(li, 0, len(li)-1):
    print ("The original array is {0}".format(str(li_bak)))
    print ("The quick-sorted array is {0}".format(str(li)))
    print ("The quicksort algorithm is correct!")
  else:
    print ("The original array is {0}".format(str(li_bak)))
    print ("The quick-sorted array is {0}".format(str(li)))
    print ("The quicksort algorithm is wrong!")
    
