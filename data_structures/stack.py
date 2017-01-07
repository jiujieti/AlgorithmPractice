class StackPopError(Exception):
  pass

class stack():
  
  stack = []

  def __init__(self):
    pass
  
  def isEmpty(self):
    return not self.stack

  def pop(self):
    if not self.stack:
      raise StackPopError("This stack is empty!")
    else:
      ele = self.stack[len(self.stack)-1]
      self.stack.remove(ele)
      return ele

  def push(self, a):
    self.stack.append(a)

