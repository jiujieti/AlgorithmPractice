class Node:
  
  def __init__(self, val, pre=None, succ=None):
    self.value = val
    self.pre = pre
    self.succ = succ

class DoublyLinkedList:
  
  def __init__(self, li, isCircle):
    if not li:
      self.head, self.tail = None, None
      return self.head, self.tail 
    self.head = Node(li[0])
    p = self.head
    for ele in li[1:]:
      q = Node(ele, p)
      p.succ = q
      p = q
    self.tail = p
    if isCircle:
      self.head.prev, self.tail.succ = self.tail, self.head
    else:
      self.head.prev, self.tail.succ = None, None 
    return self.head, self.tail
        
  def insert_ele(self, val):  
    q = Node(val)
    if self.head is None or val < self.head.value:
      q.succ = self.head
      q.prev = self.head.prev
      self.head.prev = q
      self.head = q
      return self.head, self.tail
    
    p = self.head
    while p is not self.tail.succ and p.value < val:
      p = p.succ
    if p is self.tail:
      q.succ = p.succ
      q.prev = p
      p.succ = q
      self.tail = q
      return self.head, self.tail
    q.prev = p.prev
    p.prev.succ = q
    q.succ = p
    p.prev = q
    return self.head, self.tail
   
  def delete_ele(self, val):
    pass

  def reverse_list(self):
    p = self.head
    q = None
    while p is not self.tail.succ:
  def return_list(self):
    li = []
    p = self.head
    while p is not self.tail:
      li.append(p.value)
      p = p.succ
    return li



  
  
