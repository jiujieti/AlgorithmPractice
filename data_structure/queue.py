class DequeueError(Exception):
  pass

class queue():
  
  queue = []

  def __init__(self):
    pass

  def isEmpty(self):
    return not self.queue

  def enqueue(self, a):
    self.queue.append(a)

  def dequeue(self):
    if not self.queue:
      raise DequeueError("This queue is empty!")
    else:
      a = self.queue[0]
      self.queue.remove(a)
      return a

