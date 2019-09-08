from constants import *
from .paren_tree import ParenNode, ParenTree

class OperationNode:
  def __init__(self, operator, left, right):
    self.operator = operator
    self.left = left
    self.right = right
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
    self.priority = p

  def __repr__(self):
    return f'OperationNode {self.priority} - [{self.left} {self.operator} {self.right}]'


class OperationsQueue:
  def __init__(self):
    self.values = []

  def __repr__(self):
    return f'OperationsQueue - {self.values}'

  def enqueue(self, node: OperationNode):
    self.values.append(node)
    self.values = sorted(self.values, key=lambda x: x.priority)

  def dequeue(self):
    if len(self.values):
      return self.values.pop(0)
    return None


