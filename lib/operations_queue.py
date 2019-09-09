from constants import *
from .paren_tree import ParenNode, ParenTree

class OperationNode:
  def __init__(self, operator, left, right):
    self.operator = operator.value
    self.left = left.value if not left.queued else ''
    self.right = right.value if not right.queued else ''
    op = operator.value
    if op == LEFT_PAREN:
      p = 1
    elif op == EXPONENT:
      p = 2
    elif op == MULTIPLY:
      p = 3
    elif op == DIVIDE:
      p = 4
    elif op == ADD:
      p = 5
    elif op == SUBTRACT:
      p = 6
    else:
      p = None
    self.priority = p

  def __repr__(self):
    return f'OperationNode {self.priority} - [{self.left} {self.operator} {self.right}]'


class OperationsQueue:
  def __init__(self, priority=None):
    self.values = []
    self.priority = priority

  def __repr__(self):
    return f'OperationsQueue - priority: {self.priority} - {self.values}'

  def enqueue(self, node: OperationNode or OperationsQueue):
    self.values.append(node)
    self.values = sorted(self.values, key=lambda x: x.priority)

  def dequeue(self):
    if len(self.values):
      return self.values.pop(0)
    return None


