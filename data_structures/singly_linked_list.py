class Node:
  
  value = None
  succ = None

  def __init__(self, val):
    self.value = val

class SinglyLinkedListError(Exception):
  pass

class SinglyLinkedList:

  head = None

  def __init__(self, li):
    if li:
      self.head = Node(li[0])
      p = self.head
      for ele in li[1:]:
        q = Node(ele)
        p.succ = q
        p = q
      p.succ = None
    else:
      self.head = Node(None)

  def insert_ele(self, val):
    #insert a element from a sorted singly linked list
    #first consider if the new node could be inserted as the list head 
    p = self.head
    q = Node(val)
    if p.value == None or val < p.value:
      q.succ = self.head.succ
      self.head = q
    else:
      #scan through the list until the next value is None or the next value is larger or equal to the one to be inserted
      while p.succ != None and p.succ.value < val:
        p = p.succ
      if p.succ == None:
        p.succ = q
        q.succ = None
      else:
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
      while p.value == val and p is not None:
        p = p.succ
      q.succ = p
      q = p 
      p = p.succ 
    return self.head

  def return_list(self):
    p = self.head
    li = []
    while p is not None:
      li.append(p.value)
      p = p.succ
    return li

