import uuid
from constants import *
from .char_list import CharList, CharListNode
from .priority_queue import PriorityQueue, PQNode
# from models.char_list import create_simple_char_list

class ParenNode:
  def __init__(self):
    self.items = []
    self.operations = PriorityQueue()

  def __repr__(self):
    return f'ParenNode: {self.items}' 
  
  def prioritize_items(self):
    item_len = len(self.items)
    paren_nodes = [x for x in self.items if type(x) is ParenNode]
    demo('Number of items in current ParenNode', item_len)
    demo('Number of ParenNodes in current ParenNode.items', len(paren_nodes))

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

          operation['operator'] = left_operator if left_is_priority else right_operator

          
            
          
          print( next_left, left, 'PARENS', right, next_right)
          # if left.value in OPERATORS:
          #   operation['operator']
          # operation['left'] = left.value
          # operation['']

        
        pq_node = PQNode(operation)
        self.operations.enqueue(pq_node)
      
      # handle non-ParenNode items in self.items
      else:
        for item in self.items:
          if type(item) is not ParenNode and not item.queued:
            print('HHUUUU', item)
      
      for node in paren_nodes:
        node.prioritize_items()



        

        # print('left', left)
        # demo('Operation dictionary', operation)
        






  # def prioritize_items(self):
  #   item_len = len(self.items)
  #   demo('Number of items in current ParenNode', item_len)
  #   for i, item in enumerate(self.items):
  #     left = self.items[i - 1] if i > 0 else None
  #     right = self.items[i + 1] if i < len(self.items) - 1 else None

  #     pq_node = PQNode()

  #     if type(item) is ParenNode: # ITEM IS PAREN_NODE
  #       if left is None: # we are at the beginning of items 
  #         # We want to look to the right of item for the operator. If the item 
  #         # to the right is not an operator, we assume the operator should be MULTIPLY. 
  #         if right.value in OPERATORS:
  #           operator = right.value
  #         else:
  #           operator = MULTIPLY
          
  #         pq_node.operator = operator
          
  #         next_to_right = self.items[i + 2]

  #         if type(next_to_right) is ParenNode: 
  #           pass
  #         elif next_to_right.value in OPERATORS:
  #           parser_error('cannot have two adjacent operators')
  #         else:
  #           pass
            
    
  #       elif right is None: # we are at the end of items
  #         pass
 
  #       else: # we are somewhere in the middle of items
  #         pass

  #     elif type(item) is CharListNode: # ITEM IS CHAR_LIST_NODE
  #       if item.value in OPERATORS:
  #         # what is the operator
  #         # what is left
  #         # what is right
  #         pq_node = PQNode()
  #         # print(left, item, right)




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


# class ParenNode:
#   def __init__(self):
#     self.text = []
#     self.children = []
  
#   def __repr__(self):
#     return f'ParenNode - text: {self.text}'


# class ParenTree:
#   def __init__(self, some_str):
#     char_list = create_simple_char_list(some_str)
#     self.root = self.build_from(char_list)

#   def __repr__(self):
#     def traverse(node: ParenNode, accum, tab):
#       accum += tab + node.__repr__() + '\n'
#       if len(node.children):
#         tab += '  '
#         for child in node.children:
#           accum += traverse(child, '', tab) 
#       return accum
#     return traverse(self.root, '', '')

#   def build_from(self, char_list: list):
#     node = ParenNode()
#     while len(char_list):
#       item = char_list.pop(0)
#       if item == LEFT_PAREN:
#         child_node = self.build_from(char_list)
#         # node.text.append(child_node)
#         node.text.append(f'PAREN_{len(node.children)}')
#         node.children.append(child_node)
#       elif item == RIGHT_PAREN:
#         return node
#       else:
#         node.text.append(item)
#     return node

  