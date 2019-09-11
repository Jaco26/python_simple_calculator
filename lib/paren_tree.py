from constants import *
from .priority_queue import PriorityQueue, PQNode

def get_from(lst, index):
  try:
    return lst[index] if index > -1 else None
  except:
    return None

class ParenNode:
  def __init__(self):
    self.items = []

  def __repr__(self):
    return f'ParNode {self.items}'



class EvaluationNode:
  def __init__(self, value):
    try:
      self.value = float(value)
    except:
      self.value = value # I think this shoul only be the case when `value` is an operator

  def __repr__(self):
    return f'EvNode {self.value}'


class ParenTree:
  def __init__(self):
    self.root = None

  def __repr__(self):
    return f'ParenTree: {self.root}'


  def parse_char_list(self, char_list: list):
    def traverse_list(lst: list):
      node = ParenNode()
      while len(lst):
        char = lst.pop(0)
        if char == LEFT_PAREN:
          paren_node_item = traverse_list(lst)
          node.items.append(paren_node_item)
        elif char == RIGHT_PAREN:
          return node
        else:
          node.items.append(char)
      return node
    
    self.root = traverse_list(char_list)
  

  def evaluate(self):
    if not self.root:
      return
    
    def create_evaluation_nodes(node: ParenNode):
      '''return a list of `EvaluationNode` instances'''
      accum = []
      for x in node.items:
        if type(x) is ParenNode:
          evaluation_result = traverse(x)
          evaluation_node = EvaluationNode(evaluation_result)
          accum.append(evaluation_node)
        else:
          evaluation_node = EvaluationNode(x)
          accum.append(evaluation_node)
      return accum


    def do_math(operator=None, left=None, right=None):
      if operator == EXPONENT:
        return left**right
      elif operator == MULTIPLY:
        return left * right
      elif operator == DIVIDE:
        return left / right
      elif operator == ADD:
        return left + right
      elif operator == SUBTRACT:
        return left - right


    def traverse(node: ParenNode):
      queue = PriorityQueue()
      visited = set()
      # Step 1:
      # Serialize all items in node.items into EvaluationNode instances.
      # Each instance has a `value` attribute which will equal the item if the item is not of type ParenNode.
      # If an item is of type ParenNode, a value will be recursively calculated for its EvaluationNode.
      evaluation_nodes = create_evaluation_nodes(node)

      # Step 2:
      # Iterate through the generated EvaluationNode list and queue operations
      for op in OPERATORS:
        for i, ev_node in enumerate(evaluation_nodes):
          if ev_node.value == op:
            left = get_from(evaluation_nodes, i - 1)
            right = get_from(evaluation_nodes, i + 1)

            if left in visited:
              left = next((x for x in queue.items if x.operation['right'] is left), None) 

            if right in visited:
              right = next((x for x in queue.items if x.operation['left'] is right), None) 
            
            operation = dict(operator=ev_node, left=left, right=right)

            queue.enqueue(PQNode(operation))

            visited.add(ev_node)
            visited.add(left)
            visited.add(right)
      
      # Step 3:
      # Do math. Iterate through the PriorityQueue instance starting at the beginning and execute
      # each PQNode.operation
      accum = 0
      while len(queue):
        item = queue.dequeue()
        operator = item['operator'].value
        left = item['left']
        right = item['right']

        if type(left) is EvaluationNode:
          left = left.value
        elif type(left) is PQNode:
          while type(left.operation['left']) is PQNode:
            left = left.operation['left']
          op = left.operation
          left = do_math(**{key: op[key].value for key in op})
          accum -= left

        if type(right) is EvaluationNode:
          right = right.value
        elif type(right) is PQNode:
          while type(right.operation['right']) is PQNode:
            right = right.operation['right']
          op = right.operation
          right = do_math(**{key: op[key].value for key in op})
          accum -= right

        accum += do_math(operator=operator, left=left, right=right)
        
      return accum

    return traverse(self.root)

      
