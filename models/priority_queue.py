
class PQNode:
  def __init__(self, value, priority):
    self.value = value
    self.priority = priority
    

class PriorityQueue:
  def __init__(self):
    self.values = []

  def enqueue(self, value, priority):
    self.values.append(PQNode(value, priority))
    self.values = sorted(self.values, key=lambda n: n.priority)

  def dequeue(self):
    return self.values.pop(0) if len(self.values) else None

