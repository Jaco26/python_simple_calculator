from constants import *

operators = ['(', ')', '*', '**', '/', '+', '-']

class PQNode:
  def __init__(self, value=[]):
    operator = next((x for x in value if x in operators))

    if operator == LEFT_PAREN:
      priority = 1
    elif operator == EXPONENT:
      priority = 2
    elif operator == MULTIPLY:
      priority = 3
    elif operator == DIVIDE:
      priority = 4
    elif operator == ADD:
      priority = 5
    elif operator == SUBTRACT:
      priority = 6

    self.value = value
    self.priority = priority
  
  def __repr__(self):
    return f'PQNode - {self.value}'
    

class PriorityQueue:
  def __init__(self):
    self.values = []

  def enqueue(self, item=[]):
    value = [x.value for x in item if not x.queued]
    self.values.append(PQNode(value))
    for x in item:
      x.queued = True
    self.values = sorted(self.values, key=lambda n: n.priority)

  def dequeue(self):
    return self.values.pop(0) if len(self.values) else None

