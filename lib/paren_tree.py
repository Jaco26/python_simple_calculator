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
        left = get_from(self.items, paren_node_i - 1)
        next_left = get_from(self.items, paren_node_i - 2)
        right = get_from(self.items, paren_node_i + 1)
        next_right = get_from(self.items, paren_node_i + 2)
        
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

        self.operations.enqueue(pq_node)
          
    for node in paren_nodes:
      node.prioritize_items()
      


class ParenTree:
  def __init__(self, some_str):
    char_list = CharList(some_str)
    self.root = self.build_from(char_list)

  def __repr__(self):
    return f'ParenTree {self.root}'

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

  def evaluate(self):

    def evaluate_children(items):
      accum = []
      for x in items:
        if type(x) is ParenNode:
          accum.append(traverse(x))
        elif type(x) is CharListNode:
          accum.append(x)
      return accum

    def traverse(node: ParenNode):
      # 1: evaluate all ParenNode children before prioritizing and executing operations
      # for any given node
      items = evaluate_children(node.items)

      demo('ITEMS from evaluate_children', items)
      
      # 2: prioritize operations
      queue = PriorityQueue()

      visited = set()

      for op in [EXPONENT, MULTIPLY, DIVIDE, ADD, SUBTRACT]:
        for i, item in enumerate(items):
          # print('ITEM', type(item))
          if type(item) is CharListNode and item.value == op:
           
            left = get_from(items, i - 1)
            right = get_from(items, i + 1)

            if left in visited:
              print('LEFT has already been visted', left)
              left = 'some_queued_item'
            
            if right in visited:
              print('RIGHT has already been visited', right)
              right = 'some_queued_item'
            
            operation = dict(operator=item, left=left, right=right)

            queue.enqueue(PQNode(operation))

            visited.add(left)
            visited.add(right)
        
      # 3: execute operations
      accum = 0
      while len(queue):
        item = queue.dequeue()
        operator = item['operator']
        left = to_number(item['left'])
        right = to_number(item['right'])


        # print('**************', to_number(left), operator, to_number(right))

        # print(left, operator, right)
        # # print()
        # if type(left) is not PQNode:
        #   left = float(left)
        # else:
        #   pass

        # if type(right) is not PQNode:
        #   right = float(right)
        # else:
        #   pass

        if operator == EXPONENT:
          accum += left**right
        elif operator == MULTIPLY:
          accum += left * right
        elif operator == DIVIDE:
          accum += left / right
        elif operator == ADD:
          accum += left + right
        elif operator == SUBTRACT:
          accum += left - right

        # print('accccum', accum)
        return accum
        # demo('DEQUEUED OPERATION', item)
      

    return traverse(self.root)


