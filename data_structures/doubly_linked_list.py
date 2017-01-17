class Node:
  
  def __init__(self, value, prev=None, succ=None):
    self.value = value
    self.prev = prev
    self.succ = succ

class DoublyLinkedListError(Exception):
  pass

class DoublyLinkedList:
  
  def __init__(self, li):
    if not li:
      self.head, self.tail = None, None
      return
    self.head = Node(li[0])
    p = self.head
    for ele in li[1:]:
      q = Node(ele, p)
      p.succ = q
      p = q
    self.tail = p
        
  def insert_ele(self, val):
    q = Node(val)
    if self.head is None:
      self.head = self.tail = q
    elif self.head.value >= val:
      self.head.prev = q
      q.succ = self.head
      self.head = q
    else:
      p = self.head
      while p is not None and p.value < val:
        p = p.succ 
      if p is None:
        q.prev = self.tail 
        self.tail.succ = q
        self.tail = q
      else:  
        q.prev = p.prev
        p.prev.succ = q
        q.succ = p
        p.prev = q

  def delete_ele(self, val):
    while self.head is not None and self.head.value == val:
      self.head = self.head.succ
    if self.head is None:
      self.tail = None
      return
    p = self.head
    q = p.succ
    while q is not None:
      while q is not None and q.value == val:
        q = q.succ
      if q is None:
        p.succ = None
        self.tail = p
        break
      else:
        p.succ = q
        q.prev = p
        p = q
        q = q.succ

  def reverse_list(self):
    p = self.head
    self.tail = p
    q = None
    while p is not None:
      q = Node(p.value, p.succ, q) 
      p = p.succ
      if p is None:
        self.head = q
        break
    return self.head, self.tail 

  def return_list(self):
    li = []
    p = self.head
    while p is not None:
      li.append(p.value)
      p = p.succ
    return li
