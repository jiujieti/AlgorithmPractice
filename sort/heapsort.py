from random import randint

def build_max_heap_property(A, heapsize, i):
  largest = i
  left = 2*i + 1
  right = 2*i + 2
  if left < heapsize and A[left] > A[largest]:
    largest = left
  if right < heapsize and A[right] > A[largest]:
    largest = right
  if largest != i:
    A[i], A[largest] = A[largest], A[i]
    build_max_heap_property(A, heapsize, largest)  

def build_max_heap(A):
  for i in range(len(A) // 2, -1, -1):
    build_max_heap_property(A, len(A), i)
    
def heapsort(A):
  build_max_heap(A)
  heapsize = len(A)
  for i in range(len(A)-1, 0, -1):
    A[i], A[0] = A[0], A[i]
    heapsize -= 1
    build_max_heap_property(A, heapsize, 0)
  return A

tests = []
for i in range(0, 5):
  A = [randint(-100, 100) for i in range(randint(0, 1000))]
  tests.append(A)
tests.append([])

for A in tests:
  A_bak = A.copy()
  A_heapsorted = heapsort(A)
  if A_heapsorted == sorted(A_bak):
    print ("The original list is {0}".format(str(A_bak)))
    print ("The heap-sorted list is {0}".format(str(A_heapsorted)))
    print ("The heapsort algorithm is correct!")
  else:
    print ("The original list is {0}".format(str(A_bak)))
    print ("The heap-sorted list is {0}".format(str(A_heapsorted)))
    print ("The heapsort algorithm is wrong.")
