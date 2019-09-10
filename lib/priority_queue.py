from constants import *


def determine_priority(operator):
  if operator == LEFT_PAREN:
    p = 1
  elif operator == EXPONENT:
    p = 2
  elif operator == MULTIPLY:
    p = 3
  elif operator == DIVIDE:
    p = 4
  elif operator == ADD:
    p = 5
  elif operator == SUBTRACT:
    p = 6
  else:
    p = None
  return p


class PQNode:
  def __init__(self, operation):
    self.operation = operation
    self.priority = determine_priority(operation['operator'].value)

  def __repr__(self):
    return f'PQNode {self.priority} [{self.operation}]'


class PriorityQueue:
  def __init__(self):
    self.items = []

  def __repr__(self):
    return f'PriorityQueue - {self.items}'
  
  def __len__(self):
    return len(self.items)

  def enqueue(self, node):
    self.items.append(node)
    self.items = sorted(self.items, key=lambda x: x.priority)
  
  def dequeue(self):
    return self.items.pop(0).operation if len(self) else None