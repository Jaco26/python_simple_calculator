
import uuid
from constants import *
from .char_list import CharList
from .paren_tree import ParenNode, ParenTree
from .operations_queue import OperationsQueue, OperationNode

def get_from(lst, index):
  if index < len(lst) and index > -1:
    return lst[index]
  return None

def is_operator(x):
  if x == EXPONENT:
    return EXPONENT
  elif x == MULTIPLY:
    return MULTIPLY
  elif x == DIVIDE:
    return DIVIDE
  elif x == ADD:
    return ADD
  elif x == SUBTRACT:
    return SUBTRACT
  else:
    return False 

class OperationsTree:
  def __init__(self, expression):
    paren_tree = ParenTree(expression)
    queue_accum = OperationsQueue()

    demo('PAREN TREE INSIDE OperationsTree __init__', paren_tree)

    self.root = self.map_from_paren_tree(paren_tree.root, queue_accum)
  

  def map_from_paren_tree(self, node: ParenNode, queue: OperationsQueue):
  
    char_list = CharList(''.join(node.text))

    for i, item in enumerate(char_list):
      left = char_list.get(i - 1)
      right = char_list.get(i + 1)

      if item.value.startswith('PAREN_'):
        paren_i = int(item.value.split('_')[1])

        paren_node = node.children[paren_i]

        paren_node_queue = self.map_from_paren_tree(paren_node, OperationsQueue(priority=1))

        queue.enqueue(paren_node_queue)

      elif item.value in OPERATORS:

        op_node = OperationNode(item, left, right)

        item.queued = True
        left.queued = True
        right.queued = True

        queue.enqueue(op_node)

    return queue
  
    