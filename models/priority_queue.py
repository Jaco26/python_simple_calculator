from constants import *

operators = ['(', ')', '*', '**', '/', '+', '-']

class PQNode:
  def __init__(self, value):
    operator = next((x for x in value if x in operators))

    if operator == MULTIPLY:
      priority = 1
    elif operator == DIVIDE:
      priority = 2
    elif operator == ADD:
      priority = 3
    elif operator == SUBTRACT:
      priority = 4

    self.value = value
    self.priority = priority
  
  def __repr__(self):
    return f'PQNode - {self.value}'
    

class PriorityQueue:
  def __init__(self):
    self.values = []

  def enqueue(self, *args):
    value = [x.value for x in args if not x.queued]
    self.values.append(PQNode(value))
    self.values = sorted(self.values, key=lambda n: n.priority)

  def dequeue(self):
    return self.values.pop(0) if len(self.values) else None

