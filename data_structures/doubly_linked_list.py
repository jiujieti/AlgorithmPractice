class Node:
  
  value = None
  prev = None
  succ = None

  def __init__(self, val):
    self.value = val

class DoublyLinkedList:
  
  head = None

  def __init__(self, li):
    if li:
      head = Node(li[0])
      p = head
      for ele in li:
        q = Node(ele)
        q.prev = p
        q.succ 
        
        



  
  
