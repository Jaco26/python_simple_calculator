from constants import *
from .paren_tree import ParenNode, ParenTree
from .operations_queue import OperationsQueue, OperationNode

class OperationsTree:
  def __init__(self, expression):
    paren_tree = ParenTree(expression)

    demo('PAREN TREE INSIDE OperationsTree __init__', paren_tree)

    self.root = self.map_from_paren_tree(paren_tree.root)
  
  def map_from_paren_tree(self, node: ParenNode):
    get = lambda lst, idx: lst[idx] if idx < len(lst) and idx > -1 else None
    queue = OperationsQueue()
    for i, x in enumerate(node.text):
      item = x
      left = get(node.text, i - 1)
      right = get(node.text, i + 1)
       
    return 'HIII'
  
    