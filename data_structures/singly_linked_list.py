class Node:
  
  value = None
  succ = None

  def __init__(self, val):
    self.value = val

class SinglyLinkedList():

  head = None

  def __init__(self, li):
    if li:
      self.head = Node(li[0])
      p = self.head
      for ele in li[1:len(li)-1]:
        q = Node(ele)
        p.succ = q
        p = q
      p.succ = None
    else:
      self.head = Node(None)

   def delete_ele(self, val):
     #delete a element from a sorted singly linked list
     #first consider if the new node could be inserted as the list head 
     p = self.head
     q = Node(val)
     if p.value == None or val < p.value:
       q.succ = self.head.succ
       self.head = q
     elif:
       #if p is not the end of the list, then we keep scan through the list 
         

   def insert_ele(self, val):
     pass
            
        
 
