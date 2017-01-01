from random import randint

def build_max_heap_property(li, heapsize, i):
  largest = i
  left = 2*i + 1
  right = 2*i + 2
  if left < heapsize and li[left] > li[largest]:
    largest = left
  if right < heapsize and li[right] > li[largest]:
    largest = right
  if largest != i:
    li[i], li[largest] = li[largest], li[i]
    build_max_heap_property(li, heapsize, largest)  

def build_max_heap(li):
  for i in range(len(li) // 2, -1, -1):
    build_max_heap_property(li, len(li), i)
    
def heapsort(li):
  build_max_heap(li)
  heapsize = len(li)
  for i in range(len(li)-1, 0, -1):
    li[i], li[0] = li[0], li[i]
    heapsize -= 1
    build_max_heap_property(li, heapsize, 0)
  return li

tests = []
for i in range(0, 5):
  li = [randint(-100, 100) for i in range(randint(0, 1000))]
  tests.append(li)
tests.append([])

for li in tests:
  li_bak = li.copy()
  li_heapsorted = heapsort(li)
  if li_heapsorted == sorted(li_bak):
    print ("The original list is {0}".format(str(li_bak)))
    print ("The heap-sorted list is {0}".format(str(li_heapsorted)))
    print ("The heapsort algorithm is correct!")
  else:
    print ("The original list is {0}".format(str(li_bak)))
    print ("The heap-sorted list is {0}".format(str(li_heapsorted)))
    print ("The heapsort algorithm is wrong.")
