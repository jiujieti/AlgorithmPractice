class Node:
  def __init__(self, val, succ=None):
    self.value = val
    self.succ = succ

class SinglyLinkedListError(Exception):
  pass

class SinglyLinkedList:
  def __init__(self, li):
    if not li:
      self.head = None
    else:
      self.head = Node(li[0])
      p = self.head
      for ele in li[1:]:
        q = Node(ele)
        p.succ = q
        p = q
      p.succ = None
    return self.head

  def insert_ele(self, val):
    """Insert a element, assuming that this is a sorted singly linked list."""
    
    # First consider if the new node could be inserted as the list head.
    q = Node(val)
    if self.head == None or val < self.head.value:
      q.succ = self.head
      self.head = q
      return self.head

    # Walk through the list until the next value is None or the next value is larger or equal to the one to be inserted
    p = self.head
    while p.succ != None and p.succ.value < val:
      p = p.succ
    q.succ = p.succ
    p.succ = q
    return self.head

  def delete_ele(self, val):
    p = self.head
    if not p:
      raise SinglyLinkedListError("Empty List! No elements found.")   
    while p.value == val:
      p = p.succ
    self.head = p
    q = p
    p = p.succ
    while p is not None:
      while p is not None and p.value == val:
        p = p.succ
      q.succ = p
      q = p 
      p = p.succ 
    return self.head
 
  def reverse_list(self):
    p = self.head
    q = None
    while p is not None:
      q = Node(p.value, q)    
      p = p.succ      
    self.head = q
    return self.head

  def return_list(self):
    p = self.head
    li = []
    while p is not None:
      li.append(p.value)
      p = p.succ
    return li

