import uuid
from constants import *
from .char_list import CharList, CharListNode
from .priority_queue import PriorityQueue, PQNode
# from models.char_list import create_simple_char_list

def get_from(lst, index):
  try:
    return lst[index] if index > -1 else None
  except:
    return None

class ParenNode:
  def __init__(self):
    self.items = []
    self.operations = PriorityQueue()

  def __repr__(self):
    return f'ParenNode: {self.items}' 
  
  def prioritize_items(self):
    item_len = len(self.items)
    paren_nodes = [x for x in self.items if type(x) is ParenNode]

    # handle ParenNode instances in self.items
    if len(paren_nodes):
      paren_node_indexes = [self.items.index(x) for x in paren_nodes]
      for paren_node_i in paren_node_indexes:
        paren_node = self.items[paren_node_i]
        left = self.items[paren_node_i - 1] if paren_node_i > 0 else None
        next_left = self.items[paren_node_i - 2] if paren_node_i > 1 else None
        right = self.items[paren_node_i + 1] if paren_node_i < len(self.items) - 1 else None
        next_right = self.items[paren_node_i + 2] if paren_node_i < len(self.items) - 2 else None
        
        operation = {}

        if not left: # no item is to the left of the ParenNode
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
        self.operations.enqueue(pq_node)
      
    # handle non-ParenNode items in self.items
    for i, item in enumerate(self.items):
      if type(item) is not ParenNode and not item.queued and item.value in OPERATORS:
        
        left = get_from(self.items, i - 1)
        right = get_from(self.items, i + 1)

        operation = {
          'operator': item.value,
          'left': left.value if type(left) is not ParenNode and not left.queued else 'SOME_PAREN_NODE',
          'right': right.value if type(right) is not ParenNode and not right.queued else 'SOME_PAREN_NODE',
        }

        pq_node = PQNode(operation)

        self.operations.enqueue(pq_node)

        # print_this = f'left={left.value + "(Qd)" if left.queued else left.value}\n' if type(left) is CharListNode else 'left=ParenNode\n'
        # print_this += f'item={item.value + "(Qd)" if item.queued else item.value}\n' if type(item) is CharListNode else 'item=ParenNode\n'
        # print_this += f'right={right.value + "(Qd)" if right.queued else right.value}\n' if type(right) is CharListNode else 'right=ParenNode\n'
        # print(print_this)
          
    for node in paren_nodes:
      node.prioritize_items()
      


class ParenTree:
  def __init__(self, some_str):
    char_list = CharList(some_str)

    self.root = self.build_from(char_list)

    self.root.prioritize_items()

  def __repr__(self):
    return f'ParenTree {self.root.items}'

  
  def build_from(self, char_list: CharList):
    node = ParenNode()
    while len(char_list):
      char = char_list.shift()
      if char.value == LEFT_PAREN:
        node.items.append(self.build_from(char_list))
      elif char.value == RIGHT_PAREN:
        return node
      else:
        node.items.append(char)
    return node
