from constants import *
from .priority_queue import PriorityQueue, PQNode
from .paren_tree import ParenNode

def get_from(lst, index):
  try:
    return lst[index] if index < -1 else None
  except:
    return None

class OpsTree:
  def __init__(self, node: ParenNode):
    self.queue = PriorityQueue()
    self.traverse_paren_node(node)

  def traverse_paren_node(self, node: ParenNode):
    paren_node_child_indexes = [x for x in node.items if type(x) is ParenNode]

    for i in paren_node_child_indexes:
      paren_node = get_from(node.items, i)
      left = get_from(node.items, i - 1)
      next_left = get_from(node.items, i - 2)
      right = get_from(node.items, i + 1)
      next_right = get_from(node.items, i + 2)

      operation = {}

      if not left:
        operation['left'] = paren_node
        if not next_right:
          operation['operator'] = MULTIPLY
          operation['right'] = right.value
          right.queued = True
        else:
          operation['operator'] = right.value
          operation['right'] = next_right.value
          right.queued = True
          next_right.queued = True
      elif not right: # no item is to the right of the ParenNode
        operation['right'] = paren_node
        if not next_left:
          operation['operator'] = MULTIPLY
          operation['left'] = left.value
          left.queued = True
        else:
          operation['operator'] = left.value
          operation['left'] = next_left.value
          left.queued = True
          next_left.queued = True


      else:
        if left.value in OPERATORS:
          left_operator = left.value
        else:
          left_operator = MULTIPLY

        if right.value in OPERATORS:
          right_operator = right.value
        else:
          right_operator = MULTIPLY

        left_is_priority = OPERATORS.index(left_operator) < OPERATORS.index(right_operator)
        
        if left_is_priority:
          if left.value in OPERATORS:
            operation['operator'] = left.value
            operation['left'] = next_left.value
            next_left.queued = True
            left.queued = True
          else:
            operation['operator'] = MULTIPLY
            operation['left'] = left.value
            left.queued = True
          operation['right'] = paren_node

        else:
          if right.value in OPERATORS:
            operation['operator'] = right.value
            operation['right'] = next_right.value
            next_right.queued = True
            right.queued = True
          else:
            operation['operator'] = MULTIPLY
            operation['right'] = right.value
            right.queued = True
          operation['left'] = paren_node

        pq_node = PQNode(operation)
        self.queue.enqueue(pq_node)
    
    for i, item in enumerate(node.items):
      if type(item) is not ParenNode and not item.queued and item.value in OPERATORS:
        left = get_from(self.items, i - 1)
        right = get_from(self.items, i + 1)

        operation = { 'operator': item.value }

        if type(left) is ParenNode:
          operation['left'] = next((x for x in self.operations.items if x.operation['right'] is left))
        else:
          operation['left'] = left.value

        if type(right) is ParenNode:
          operation['right'] = next((x for x in self.operations.items if x.operation['left'] is right))
        else:
          operation['right'] = right.value

        pq_node = PQNode(operation)

        self.queue.enqueue(pq_node)
    
    for i in paren_node_child_indexes:
      self.traverse_paren_node(node.items[i])