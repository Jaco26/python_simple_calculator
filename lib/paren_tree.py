from constants import *
from .priority_queue import OperationQueue, OperationNode

def get_from(lst, index):
  try:
    return lst[index] if index > -1 else None
  except:
    return None

def should_prioritize_op(o1, o2):
  if o1 in [MULTIPLY, DIVIDE] and o2 in [ADD, SUBTRACT]:
    return True
  return False


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
      self.value = value # this should only be the case when `value` is an operator

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


    def do_math(operation: OperationNode = None, **kwargs):
      if operation:
        left = operation.left.value
        right = operation.right.value
        operator = operation.operator.value
      else:
        left = kwargs.get('left')
        right = kwargs.get('right')
        operator = kwargs.get('operator')
      if operator == EXPONENT:
        return left**right
      elif operator == MULTIPLY:
        return left * right
      elif operator == DIVIDE:
        return left / right if right != 0 else 0
      elif operator == ADD:
        return left + right
      elif operator == SUBTRACT:
        return left - right

    def traverse(node: ParenNode):
      queue = OperationQueue()
      visited = set()
      # Step 1:
      # Serialize all items in node.items into EvaluationNode instances.
      # Each instance has a `value` attribute which will equal the item if the item is not of type ParenNode.
      # If an item is of type ParenNode, a value will be recursively calculated for its EvaluationNode.
      evaluation_nodes = create_evaluation_nodes(node)
      demo('Evaluation Nodes', evaluation_nodes)

      # Find all operators in evaluation_nodes
      # exp_ops = [{ 'index': i, 'value': evaluation_nodes[i].value } for i, x in enumerate(evaluation_nodes) if x.value == EXPONENT ]
      # mult_div_ops = [(i, evaluation_nodes[i]) for i, x in enumerate(evaluation_nodes) if x.value in [MULTIPLY, DIVIDE]]
      # add_sub_ops = [(i, evaluation_nodes[i]) for i, x in enumerate(evaluation_nodes) if x.value in [ADD, SUBTRACT]]
      
      # # Queue operation nodes
      # for op in exp_ops:
      #   pass

      # for i, (item_i, item) in enumerate(mult_div_ops):
      #   left = get_from(evaluation_nodes, item_i - 1)
      #   right = get_from(evaluation_nodes, item_i + 1)

      #   if left in visited:
      #     left = queue.find_where(lambda x: x.right is left)
      #     # left = do_math(left)
      #     # print('LEFT VISITED', left)
        
      #   if right in visited:
      #     right = queue.find_where(lambda x: x.left is right)
      #     # right = do_math(right)
      #     # print('RIGHT VISITED', left)

      #   operation = OperationNode(operator=item, operator_index=i, left=left, right=right)
      #   queue.enqueue(operation)

      #   visited.add(item)
      #   visited.add(left)
      #   visited.add(right)
      
      # for i, (item_i, item) in enumerate(add_sub_ops):
      #   left = get_from(evaluation_nodes, item_i - 1)
      #   right = get_from(evaluation_nodes, item_i + 1)

      #   if left in visited:
      #     left = queue.find_where(lambda x: x.right is left)
      #     # left = do_math(left)
      #     # print('LEFT VISITED', left)
        
      #   if right in visited:
      #     right = queue.find_where(lambda x: x.left is right)
      #     # right = do_math(right)
      #     # print('RIGHT VISITED', right)

      #   operation = OperationNode(operator=item, operator_index=i, left=left, right=right)
      #   queue.enqueue(operation)

      #   visited.add(item)
        # visited.add(left)
        # visited.add(right)

      print(queue)


      # # Step 2:
      # # Iterate through the generated EvaluationNode list and queue operations
      # for i, ev_node in enumerate(evaluation_nodes):
      #   # if ev_node.value == op:
      #   if ev_node.value in OPERATORS:
      #     left = get_from(evaluation_nodes, i - 1)
      #     right = get_from(evaluation_nodes, i + 1)

      #     while left in visited:
      #       left = queue.find_where(lambda x: x.right is left)

      #     # print('NEW LEFT', left)

      #     if right in visited:
      #       right = queue.find_where(lambda x: x.left is right)

      #     operation = dict(operator=ev_node, operator_index=i, left=left, right=right)

      #     queue.enqueue(OperationNode(**operation))

      #     visited.add(ev_node)
      #     visited.add(left)
      #     visited.add(right)

      # demo('This is the Queue before doing maths', queue)
      
      # Step 3:
      # Do math. Iterate through the PriorityQueue instance starting at the beginning and execute
      # each PQNode.operation
      accum = 0
      while len(queue):
        item = queue.dequeue() # OperationNode
        operator = item.operator.value
        left = item.left
        right = item.right

        if type(left) is EvaluationNode:
          left = left.value
        elif type(left) is OperationNode:
          while type(left.left) is OperationNode:
            left = left.left
          left = do_math(left)
          accum -= left

        if type(right) is EvaluationNode:
          right = right.value
        elif type(right) is OperationNode:
          while type(right.right) is OperationNode:
            right = right.right
          right = do_math(right)
          accum -= right

        result = do_math(operator=operator, left=left, right=right)
        accum += result
        # print(left, operator, right, '=', result)
        # print('ACCUM + RESULT =', accum)
        # print()
        
      return accum

    return traverse(self.root)

      
