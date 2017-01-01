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

A = [2, 5, 3, 1, 4]
print (str(heapsort(A)))
