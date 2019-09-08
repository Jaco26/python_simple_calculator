from constants import *
from models import CharList

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


class OperationQueue:
  def __init__(self):
    self.values = []
  
  def __repr__(self):
    return f'OperationQueue:\n\t{self.values}'

  def enqueue(self, node):
    self.values.append(node)
    self.values = sorted(self.values, key=lambda x: x.priority)

  def dequeue(self):
    if len(self.values):
      return self.values.pop(0)
    return None


class OperationsTree:
  def __init__(self, some_str):
    self.operations = self.build_queue_from(CharList(some_str))

  def __repr__(self):
    return f'OperationsTree:\n\t{self.operations}'

  def build_queue_from(self, char_list: CharList):
    queue = OperationQueue()
    for op in OPERATORS:
      for i, (item, left, right) in enumerate(char_list):
        if item.value == op:
          if op == LEFT_PAREN:
            # handle left paren
            node = OperationNode(LEFT_PAREN, left, self.build_queue_from(char_list.get_slice(i)))
            queue.enqueue(node)
          elif op == RIGHT_PAREN:
            # handle right paren
            return queue
            # pass
          else:
            node = OperationNode(op, left, right)
            queue.enqueue(node)
            return queue
    return queue



class ParenNode:
  def __init__(self):
    self.text = []
    self.children = []

  def __repr__(self):
    return f'ParenNode - {self.text} - children: {len(self.children)}'

class ParenTree:
  # this class handles parsing the whole expression into appropriate scopes
  # by parentheses
  def __init__(self, some_str):
    self.root = self.build_from([x.value for x in CharList(some_str)._items])

  def build_from(self, char_list: list):
    node = ParenNode()
    while len(char_list):
      item = char_list.pop(0)
      if item == LEFT_PAREN:
        child_node = self.build_from(char_list)
        node.children.append(child_node)
      elif item == RIGHT_PAREN:
        return node
      else:
        node.text.append(item)
    return node

  def display(self):
    def traverse(node: ParenNode, tab=''):
      print(tab, node)
      if len(node.children):
        tab += '  '
        for child in node.children:
          traverse(child, tab)
    traverse(self.root)

    



  


def testy_westy():
  '''
  for each parenthetical scope, all operators must be searched out in proper order
  '''

  char_list = CharList(some_str)
  demo('CHAR LIST BEFORE SPLICE', char_list)
  smaller = char_list.splice(2, 5)
  demo('CHAR LIST AFTER SPLICE AT INDEX 2, 5', char_list)
  demo('VALUE RETURNED FROM SPLICE', smaller)
  print(char_list)
  print(smaller)

